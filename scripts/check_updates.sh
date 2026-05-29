#!/usr/bin/env sh
# Check whether this Mira checkout is behind its configured upstream.

set -eu

usage() {
  cat <<'EOF'
Usage: scripts/check_updates.sh [--no-fetch] [--prompt]

Checks whether the current branch has remote updates.

Options:
  --no-fetch   Do not contact the remote; compare against local remote-tracking refs only.
  --prompt     If the branch is behind, ask whether to run `git pull --ff-only`.

The script never updates the repository unless --prompt is used and the user
explicitly answers yes.
EOF
}

fetch_remote=1
prompt_update=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    --no-fetch)
      fetch_remote=0
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

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not inside a git work tree." >&2
  exit 2
fi

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

if [ "$fetch_remote" -eq 1 ]; then
  echo "Checking remote updates from '$remote'..."
  if ! git fetch --quiet "$remote"; then
    echo "Could not fetch '$remote'. Continue with existing local refs." >&2
  fi
else
  echo "Skipping network fetch; comparing local refs only."
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
