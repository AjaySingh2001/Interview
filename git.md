Below is a **Git Basic Sheet** with **daily-used commands**, arranged **from low → high difficulty**, written in a **clean interview + real-work style**.
(Short, clear, and practical ✅)

---

## ✅ Git Basic Sheet (Low → High Difficulty)

---

## 🔰 Level 1: Absolute Basics (Daily Use)

| Command                   | Purpose                                         |
| ------------------------- | ----------------------------------------------- |
| `git --version`           | Check Git version                               |
| `git init`                | Initialise a new Git repository                 |
| `git status`              | Check file status (modified, staged, untracked) |
| `git add file.txt`        | Stage a specific file                           |
| `git add .`               | Stage all changes                               |
| `git commit -m "message"` | Commit staged changes                           |
| `git log`                 | View commit history                             |
| `git log --oneline`       | Compact commit history                          |

---

## 🔰 Level 2: Working With Files & History

| Command                         | Purpose                        |
| ------------------------------- | ------------------------------ |
| `git diff`                      | Show unstaged changes          |
| `git diff --staged`             | Show staged changes            |
| `git show commit_id`            | View a specific commit         |
| `git rm file.txt`               | Remove file and stage deletion |
| `git mv old new`                | Rename/move file               |
| `git restore file.txt`          | Discard local changes          |
| `git restore --staged file.txt` | Unstage a file                 |

---

## 🔰 Level 3: Branching (Very Common in Teams)

| Command                       | Purpose                   |
| ----------------------------- | ------------------------- |
| `git branch`                  | List branches             |
| `git branch branch_name`      | Create new branch         |
| `git checkout branch_name`    | Switch branch             |
| `git checkout -b branch_name` | Create + switch branch    |
| `git switch branch_name`      | Safer branch switching    |
| `git merge branch_name`       | Merge branch into current |
| `git branch -d branch_name`   | Delete branch             |

---

## 🔰 Level 4: Remote Repositories (GitHub / GitLab)

| Command                          | Purpose               |
| -------------------------------- | --------------------- |
| `git remote -v`                  | Show remote URLs      |
| `git remote add origin URL`      | Add remote repository |
| `git push origin branch_name`    | Push changes          |
| `git push -u origin branch_name` | Push + set upstream   |
| `git pull`                       | Fetch + merge changes |
| `git fetch`                      | Download changes only |
| `git clone URL`                  | Clone a repository    |

---

## 🔰 Level 5: Undo & Fix Mistakes (Very Important)

| Command                    | Purpose                             |
| -------------------------- | ----------------------------------- |
| `git reset file.txt`       | Unstage file                        |
| `git reset --soft HEAD~1`  | Undo commit (keep changes staged)   |
| `git reset --mixed HEAD~1` | Undo commit (keep changes unstaged) |
| `git reset --hard HEAD~1`  | Fully remove commit ⚠️              |
| `git commit --amend`       | Edit last commit                    |
| `git revert commit_id`     | Safely undo commit                  |

---

## 🔰 Level 6: Stash & Temporary Work

| Command           | Purpose                  |
| ----------------- | ------------------------ |
| `git stash`       | Save uncommitted changes |
| `git stash list`  | List stashes             |
| `git stash pop`   | Apply & remove stash     |
| `git stash apply` | Apply stash (keep it)    |
| `git stash drop`  | Delete stash             |

---

## 🔰 Level 7: Advanced Daily-Use (Team-Level)

| Command                     | Purpose                 |
| --------------------------- | ----------------------- |
| `git rebase branch_name`    | Re-apply commits on top |
| `git rebase -i HEAD~n`      | Edit commit history     |
| `git cherry-pick commit_id` | Apply specific commit   |
| `git tag v1.0`              | Create version tag      |
| `git tag`                   | List tags               |
| `git blame file.txt`        | See who changed what    |

---

## 🔰 Level 8: Debugging & Cleanup (Advanced)

| Command         | Purpose                          |
| --------------- | -------------------------------- |
| `git reflog`    | Recover lost commits             |
| `git clean -f`  | Remove untracked files           |
| `git clean -fd` | Remove untracked files + folders |
| `git fsck`      | Repository integrity check       |
| `git gc`        | Garbage collection               |

---

## ✅ Most Used Commands (Interview Favourite ⭐)

```bash
git status
git add .
git commit -m "message"
git pull
git push
git checkout -b feature
git merge
git stash
git reset
git revert
```

---
