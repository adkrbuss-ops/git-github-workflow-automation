# Git and GitHub Workflow Automation

A beginner-friendly Python Task Manager project created to practice Git, GitHub collaboration workflows, and GitHub Actions automation.

## 1. Project overview

This project is a small command-line application that lets users:

- Add tasks
- View all tasks
- Mark tasks as completed

The main learning objective is not the complexity of the application. It is to understand how developers manage code changes and automate quality checks using Git and GitHub.

## 2. Project structure

```text
git-github-workflow-automation/
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── tests/
│   └── test_app.py
├── .gitignore
├── app.py
└── README.md
```

## 3. Prerequisites

Install the following:

- Python 3.10 or newer
- Git
- A GitHub account

Check your installations:

```bash
python --version
git --version
```

## 4. Run the application locally

Clone your repository:

```bash
git clone https://github.com/YOUR_USERNAME/git-github-workflow-automation.git
cd git-github-workflow-automation
```

Run the application:

```bash
python app.py
```

Run the automated tests:

```bash
python -m unittest discover -s tests -v
```

No third-party Python packages are required.

## 5. Git workflow

### Step 1: Initialize the repository

If you are creating the repository locally first:

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit: add task manager"
```

Create an empty GitHub repository with the same project name, then connect and push:

```bash
git remote add origin https://github.com/YOUR_USERNAME/git-github-workflow-automation.git
git push -u origin main
```

If you created the GitHub repository with a README or other files, clone it first instead of initializing a separate repository.

### Step 2: Create a feature branch

Avoid making every change directly on `main`.

```bash
git switch -c feature/add-task-validation
```

Make a change in `app.py`, then stage and commit it:

```bash
git add app.py
git commit -m "Add task input validation"
git push -u origin feature/add-task-validation
```

### Step 3: Create a Pull Request

1. Open your repository on GitHub.
2. Select **Compare & pull request** for your pushed branch.
3. Set the base branch to `main`.
4. Add a description of your changes.
5. Create the Pull Request.
6. Wait for the GitHub Actions check to finish.
7. Merge the Pull Request if the checks pass.

### Step 4: Update your local main branch

After merging:

```bash
git switch main
git pull origin main
```

You can delete the feature branch after merging:

```bash
git branch -d feature/add-task-validation
```

## 6. GitHub Actions automation

Workflow file: `.github/workflows/python-ci.yml`

The workflow runs automatically when:

- Code is pushed to `main` or `develop`.
- A Pull Request targets `main` or `develop`.

The workflow performs these steps:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Runs all unit tests.
4. Reports success or failure in the GitHub Actions tab and Pull Request checks.

A failed test causes the workflow to fail, helping prevent broken changes from being merged unnoticed. This workflow reports test results; it does not automatically block merging unless branch protection or a ruleset requires the check.

## 7. Important Git commands

| Command | Purpose |
|---|---|
| `git status` | Check changed files |
| `git add .` | Stage changes |
| `git commit -m "message"` | Save a commit |
| `git log --oneline` | View commit history |
| `git branch` | List branches |
| `git switch -c branch-name` | Create and switch branches |
| `git pull` | Download and integrate remote changes |
| `git push` | Upload commits to GitHub |
| `git diff` | Review unstaged changes |

## 8. Expected result

After pushing code or opening a Pull Request, go to:

**GitHub repository → Actions → Python CI**

You should see the workflow execute and the unit tests pass.

## 9. Learning outcomes

After completing this project, you should understand:

- How Git tracks source-code changes.
- How to create and manage feature branches.
- How to write meaningful commit messages.
- How to push code to GitHub.
- How Pull Requests support collaboration and code review.
- How GitHub Actions automates testing.
- Why `.gitignore` is important for keeping repositories clean.

## 10. Suggested improvements

Once the basic project works, try these improvements:

- Add a `requirements.txt` if you introduce third-party packages.
- Add a code-formatting check using `black` or `ruff`.
- Add a `develop` branch and use Pull Requests to merge into `main`.
- Add a GitHub Issue template for reporting bugs.
- Add a Pull Request template.
- Configure branch protection or a repository ruleset to require the CI check before merging.

---

**Internship task:** Git and GitHub Workflow Automation

**Status:** Beginner-level implementation with GitHub Actions CI testing.
