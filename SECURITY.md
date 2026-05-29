# Security Policy

Mira is a research workflow repository, not a hosted service. Security issues
usually involve accidental disclosure of secrets, private research data, paid
content, or personal/account information.

## Do Not Commit

- API keys, bearer tokens, cookies, session exports, or credentials.
- Brokerage account data, order history, position files, or tax documents.
- Paid research reports, expert-network transcripts, or licensed data dumps.
- Private emails, chat logs, phone numbers, addresses, or personal identifiers.
- Raw scrape caches when the source terms do not allow redistribution.

Use `.env` or a local secrets manager for credentials. The root `.gitignore`
excludes common local secret and archive paths, but contributors are responsible
for checking their own diffs.

## Reporting a Problem

If you find a committed secret or private dataset, open a private security
advisory if the hosting platform supports it. If private advisories are not
available, contact the maintainer privately before opening a public issue.

For already-published secrets, rotate the secret first. Removing a secret from a
later commit is not enough because Git history may still expose it.

## Supported Scope

This policy covers repository content, templates, scripts, and examples. It does
not cover investment outcomes, market data accuracy, or third-party source
availability.
