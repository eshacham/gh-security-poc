# CI/CD Security POC – Commit 1: Repo Hardening

This very simple Python “app” just prints a hello message.  
We’ve wired up a GitHub Actions workflow that **only** runs on pull_request → `main`.

👉 Next: enable **Branch protection** in Settings:
- Require pull requests
- Require this check to pass before merging
