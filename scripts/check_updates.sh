#!/usr/bin/env sh
# Check whether this Mira checkout is behind its configured upstream.

set -eu

usage() {
  cat <<'EOF'
Usage: scripts/check_updates.sh [--local-first] [--ttl-hours N] [--no-fetch] [--prompt]

Checks whether the current branch has remote updates.

Options:
  --local-first  Local-first freshness gate: only contact the remote when the
                 last fetch attempt is older than the TTL (default 24h);
                 otherwise compare against cached remote-tracking refs. Use this
                 for standard/deep_dive research so freshness is checked at most
                 once per TTL instead of once per task.
  --ttl-hours N  TTL window in hours for --local-first (default 24; 0 forces a
                 fetch attempt every run).
  --no-fetch     Never contact the remote; compare against cached remote-tracking
                 refs only. Wins over --local-first.
  --prompt       If the branch is behind, ask whether to run `git pull --ff-only`.

Freshness-check state (last attempt/success, status, remote head) is recorded in
local/mira-update-check.json (gitignored; override with MIRA_UPDATE_STATE_FILE).
A blocked or failed fetch degrades to local refs and is reported, never elevated;
the repository is never updated unless --prompt is used and the user explicitly
answers yes.
EOF
}

fetch_remote=1
prompt_update=0
local_first=0
ttl_hours=24

while [ "$#" -gt 0 ]; do
  case "$1" in
    --no-fetch)
      fetch_remote=0
      ;;
    --local-first)
      local_first=1
      ;;
    --ttl-hours)
      shift
      if [ "$#" -eq 0 ]; then
        echo "--ttl-hours requires a value." >&2
        exit 2
      fi
      ttl_hours="$1"
      ;;
    --prompt)
      prompt_update=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

case "$ttl_hours" in
  ''|*[!0-9]*)
    echo "--ttl-hours must be a non-negative integer." >&2
    exit 2
    ;;
esac

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not inside a git work tree." >&2
  exit 2
fi

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
state_file="${MIRA_UPDATE_STATE_FILE:-$repo_root/local/mira-update-check.json}"
have_python=0
if command -v python3 >/dev/null 2>&1; then
  have_python=1
fi

# Read one value from the gitignored state file. Prints nothing if the key,
# file, or python3 is unavailable, so callers must tolerate an empty result.
# Never fails the script (trailing `|| true`), so reading a freshness cache can
# only degrade to "no cache", never abort the check.
state_get() {
  [ "$have_python" -eq 1 ] || return 0
  [ -f "$state_file" ] || return 0
  python3 - "$state_file" "$1" <<'PY' || true
import json, sys
try:
    with open(sys.argv[1]) as fh:
        data = json.load(fh)
except Exception:
    sys.exit(0)
if isinstance(data, dict):
    value = data.get(sys.argv[2])
    if value is not None:
        print(value)
PY
}

# Merge key/value pairs into the state file (JSON). Keys ending in _at are
# stored as integers. A no-op when python3 is unavailable, and never fatal: an
# unwritable state path degrades to an uncached local check rather than
# aborting the freshness gate under `set -e`.
state_set() {
  [ "$have_python" -eq 1 ] || return 0
  mkdir -p "$(dirname "$state_file")" 2>/dev/null || true
  python3 - "$state_file" "$@" >/dev/null 2>&1 <<'PY' || true
import json, sys
path = sys.argv[1]
args = sys.argv[2:]
try:
    with open(path) as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        data = {}
except Exception:
    data = {}
for i in range(0, len(args) - 1, 2):
    key, value = args[i], args[i + 1]
    if key.endswith("_at"):
        try:
            value = int(value)
        except ValueError:
            pass
    data[key] = value
with open(path, "w") as fh:
    json.dump(data, fh, indent=2, sort_keys=True)
    fh.write("\n")
PY
}

branch="$(git branch --show-current)"
upstream=""
remote=""
can_pull=0

default_remote_ref() {
  candidate_remote="$1"
  default_ref="$(git symbolic-ref --quiet --short "refs/remotes/$candidate_remote/HEAD" 2>/dev/null || true)"
  if [ -n "$default_ref" ]; then
    echo "$default_ref"
    return 0
  fi

  if git rev-parse --verify --quiet "$candidate_remote/main" >/dev/null; then
    echo "$candidate_remote/main"
    return 0
  fi

  if git rev-parse --verify --quiet "$candidate_remote/master" >/dev/null; then
    echo "$candidate_remote/master"
    return 0
  fi

  return 1
}

if [ -n "$branch" ]; then
  upstream="$(git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null || true)"
  if [ -n "$upstream" ]; then
    remote="${upstream%%/*}"
    can_pull=1
  fi
fi

if [ -z "$upstream" ]; then
  remote="$(git remote | sed -n '1p')"
  if [ -z "$remote" ]; then
    if [ -z "$branch" ]; then
      echo "Current checkout is detached and no remote is configured; skip remote update check."
    else
      echo "Branch '$branch' has no configured upstream and no remote is configured; skip remote update check."
    fi
    exit 0
  fi
  upstream="$(default_remote_ref "$remote" || true)"
fi

if [ -z "$upstream" ]; then
  if [ -z "$branch" ]; then
    echo "Current checkout is detached and no default remote branch was found; skip remote update check."
  else
    echo "Branch '$branch' has no configured upstream and no default remote branch was found; skip remote update check."
    echo "Set one with: git branch --set-upstream-to <remote>/<branch>"
  fi
  exit 0
fi

# Try to refresh remote-tracking refs. Stamp every attempt (to throttle the
# next try, even on failure), but only record a successful check separately so
# the freshness verdict never trusts a fetch that was blocked.
attempt_fetch() {
  attempt_now="$(date +%s)"
  echo "Checking remote updates from '$remote'..."
  # Record the scope (upstream/remote) with every attempt so the TTL cache is
  # only honored for the same target it was taken against.
  state_set last_attempt_at "$attempt_now" upstream "$upstream" remote "$remote"
  if git fetch --quiet "$remote" 2>/dev/null; then
    fetched_head="$(git rev-parse "$upstream" 2>/dev/null || true)"
    state_set last_remote_check_at "$attempt_now" status ok remote_head "$fetched_head"
  else
    echo "Could not fetch '$remote' (network blocked or unavailable)." >&2
    echo "Mira protocol remote freshness not checked; using local refs." >&2
    state_set status fetch_failed
  fi
}

if [ "$fetch_remote" -eq 0 ]; then
  echo "Skipping network fetch; comparing cached local refs only."
elif [ "$local_first" -eq 1 ]; then
  now="$(date +%s)"
  last_attempt="$(state_get last_attempt_at || true)"
  stored_upstream="$(state_get upstream || true)"
  stored_remote="$(state_get remote || true)"
  ttl_seconds=$((ttl_hours * 3600))
  # Treat a non-numeric cached timestamp (corrupt, hand-edited, or a future
  # format) as a missing cache, so it degrades to a re-fetch rather than
  # aborting in the arithmetic below under `set -u`.
  case "$last_attempt" in ''|*[!0-9]*) last_attempt="" ;; esac
  # Honor the TTL only when the cached attempt is recent AND was taken against
  # the same upstream/remote; otherwise re-fetch for the current target.
  if [ -n "$last_attempt" ] && [ "$ttl_seconds" -gt 0 ] \
    && [ "$((now - last_attempt))" -lt "$ttl_seconds" ] \
    && [ "$stored_upstream" = "$upstream" ] && [ "$stored_remote" = "$remote" ]; then
    last_status="$(state_get status || true)"
    last_ok="$(state_get last_remote_check_at || true)"
    case "$last_ok" in ''|*[!0-9]*) last_ok="" ;; esac
    # Only claim "checked" when the last attempt actually succeeded within the
    # TTL; a recent failed attempt still throttles re-tries but must disclose
    # that remote freshness is unknown.
    if [ "$last_status" = "ok" ] && [ -n "$last_ok" ] && [ "$((now - last_ok))" -lt "$ttl_seconds" ]; then
      age_hours=$(((now - last_ok) / 3600))
      echo "Remote checked within the last ${ttl_hours}h (about ${age_hours}h ago); comparing against cached refs."
    else
      echo "Last remote fetch within the last ${ttl_hours}h did not succeed (status: ${last_status:-unknown}); not re-fetching yet." >&2
      echo "Mira protocol remote freshness not checked; using local refs." >&2
    fi
  else
    attempt_fetch
  fi
else
  attempt_fetch
fi

local_head="$(git rev-parse HEAD)"
remote_head="$(git rev-parse "$upstream")"
merge_base="$(git merge-base HEAD "$upstream")"

if [ "$local_head" = "$remote_head" ]; then
  echo "Mira is up to date with $upstream."
  exit 0
fi

if [ "$local_head" = "$merge_base" ]; then
  if [ -n "$branch" ]; then
    echo "Remote update available: '$branch' is behind $upstream."
  else
    echo "Remote update available: detached HEAD is behind $upstream."
  fi

  if [ "$can_pull" -eq 0 ]; then
    echo "Not offering automatic pull because this checkout has no branch upstream."
    echo "Switch to a branch with an upstream before updating."
  else
    echo "Review first, then update with: git pull --ff-only"
  fi

  if [ "$prompt_update" -eq 1 ] && [ "$can_pull" -eq 1 ]; then
    if [ -n "$(git status --porcelain)" ]; then
      echo "Working tree has local changes; not offering automatic pull."
      echo "Commit, stash, or discard local changes before updating."
      exit 1
    fi

    printf "Run 'git pull --ff-only' now? [y/N] "
    read answer
    case "$answer" in
      y|Y|yes|YES)
        git pull --ff-only
        ;;
      *)
        echo "Update skipped by user."
        ;;
    esac
  fi
  exit 1
fi

if [ "$remote_head" = "$merge_base" ]; then
  if [ -n "$branch" ]; then
    echo "Local branch '$branch' is ahead of $upstream; no remote update needed."
  else
    echo "Detached HEAD is ahead of $upstream; no remote update needed."
  fi
  exit 0
fi

if [ -n "$branch" ]; then
  echo "Local branch '$branch' and $upstream have diverged."
else
  echo "Detached HEAD and $upstream have diverged."
fi
echo "Do not auto-update. Review with: git status && git log --oneline --graph --decorate --all -20"
exit 1
