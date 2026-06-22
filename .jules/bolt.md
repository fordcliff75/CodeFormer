## 2024-06-22 - [Avoid out-of-scope files in PRs]
**Learning:** Adding dummy files (e.g. `basicsr/VERSION`) just to get testing commands like `python setup.py develop` to work locally can cause those files to be inadvertently included in the PR if you aren't careful. Code reviewers will flag these out-of-scope files.
**Action:** Always run `git status` right before creating a PR to ensure only files modified as part of the intended optimization are included. If testing artifacts were staged or modified, revert them (e.g. `git restore --staged <file>`) before submitting.
