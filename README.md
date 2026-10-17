# Furnova E-Commerce Backend

Furnova is a furniture e-commerce platform backend built with **Python, FastAPI, and PostgreSQL**.

This guide explains how team members can set up the project locally, configure their database, install the required dependencies, and contribute changes using Git branches and Pull Requests.

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Fork the Repository](#2-fork-the-repository)
3. [Clone Your Fork](#3-clone-your-fork)
4. [Create Your Own Branch](#4-create-your-own-branch)
5. [Create and Activate a Virtual Environment](#5-create-and-activate-a-virtual-environment)
6. [Install Dependencies](#6-install-dependencies)
7. [Install and Configure PostgreSQL](#7-install-and-configure-postgresql)
8. [Create the Environment File](#8-create-the-environment-file)
9. [Run the Application](#9-run-the-application)
10. [Verify the API](#10-verify-the-api)
11. [Git Workflow for Contributors](#11-git-workflow-for-contributors)
12. [Troubleshooting](#12-troubleshooting)

---

## 1. Prerequisites

Install the following tools before starting:

- **Git** — for version control.
- **Python** — use a version compatible with the project's dependencies.
- **PostgreSQL** — database server.
- **pgAdmin 4** — graphical interface for managing PostgreSQL.
- **PyCharm or Visual Studio Code** — recommended code editor.

Verify that Git and Python are available in your terminal:

```powershell
git --version
python --version
```

Check that PostgreSQL is installed and its database server is running before connecting through pgAdmin.

## 2. Fork the Repository

Forking creates your personal copy of the organization's repository.

1. Open the original repository:

   https://github.com/CCGP-Dev/Furniture_E-Com_Backend

2. Click **Fork** in the top-right area.
3. Select your personal GitHub account as the owner.
4. Keep the repository name as `Furniture_E-Com_Backend`.
5. Click **Create fork**.

Your fork should be available at:

```text
https://github.com/YOUR-GITHUB-USERNAME/Furniture_E-Com_Backend
```

Replace `YOUR-GITHUB-USERNAME` with your actual GitHub username.

**Why fork?**

A fork allows you to work on your own copy without directly changing the organization's main branch.

## 3. Clone Your Fork

Open PowerShell or your editor's terminal and navigate to the folder where you keep your projects.

For example:

```powershell
cd D:\CClarke\PM
```

Clone your personal fork:

```powershell
git clone https://github.com/YOUR-GITHUB-USERNAME/Furniture_E-Com_Backend.git
```

Navigate into the cloned project:

```powershell
cd Furniture_E-Com_Backend
```

Open the project in VS Code if you use it:

```powershell
code .
```

If `code` is not recognized, open the cloned folder manually using your editor.

Check the Git remote:

```powershell
git remote -v
```

The `origin` remote should point to your personal fork.

## 4. Create Your Own Branch

**Do not work directly on `main`.** Create a separate branch using your name.

First, make sure you are on the main branch and update it:

```powershell
git switch main
git pull origin main
```

Create your personal branch. For example, if your name is Akila Kasun:

```powershell
git switch -c akila-kasun
```

Verify your current branch:

```powershell
git branch
```

The output should look similar to:

```text
* akila-kasun
  main
```

The asterisk (`*`) indicates the branch you are currently using.

Use your own name when creating the branch. For example:

```powershell
git switch -c your-name
```

Use lowercase letters and hyphens rather than spaces.

**Important:** If you have already created your personal branch, you can switch to it with:

```powershell
git switch your-name
```

## 5. Create and Activate a Virtual Environment

A virtual environment keeps this project's Python dependencies separate from other projects on your computer.

Make sure your terminal is inside the project root directory.

Create the virtual environment:

```powershell
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, your terminal should show `(.venv)` at the beginning of the prompt.

For example:

```text
(.venv) PS D:\CClarke\PM\Furniture_E-Com_Backend>
```

If PowerShell blocks activation because of its execution policy, you can activate the environment using Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

If your virtual environment is already created, you do not need to create it again. Simply activate it.

## 6. Install Dependencies

The project contains a `requirements.txt` file listing the Python packages required by the backend.

Ensure that your virtual environment is activated.

Upgrade pip (optional):

```powershell
python -m pip install --upgrade pip
```

Install the project dependencies:

```powershell
python -m pip install -r requirements.txt
```

Wait for the installation to finish.

Verify the installation:

```powershell
python -m pip list
```

Check for dependency conflicts:

```powershell
python -m pip check
```

A successful dependency check should report:

```text
No broken requirements found.
```

If you add a new Python dependency during development, install it in the active `.venv` and update `requirements.txt` when appropriate:

```powershell
python -m pip install package-name
python -m pip freeze > requirements.txt
```

Review the changes to `requirements.txt` before committing them.

## 7. Install and Configure PostgreSQL

Furnova uses PostgreSQL as its database.

### Step 7.1 — Start PostgreSQL

Make sure PostgreSQL is installed and its database service is running.

Open **pgAdmin 4** and connect to your local PostgreSQL server.

You may be asked for the password you configured when installing PostgreSQL.

### Step 7.2 — Create the database

Create a database named:

```text
furnova
```

In pgAdmin:

1. Expand **Servers**.
2. Connect to your local PostgreSQL server.
3. Expand the server.
4. Right-click **Databases**.
5. Select **Create → Database**.
6. Enter `furnova` as the database name.
7. Select the appropriate owner, usually your local PostgreSQL user.
8. Click **Save**.

The database should now appear under the server's Databases section.

### Step 7.3 — Verify the database

Select the `furnova` database in pgAdmin.

You can also open the Query Tool and run:

```sql
SELECT current_database();
```

The result should be:

```text
furnova
```

**Note:** Creating the database in pgAdmin and creating database tables are two different tasks. The database must exist before the application connects to it. If the project's `init_model()` function creates tables at application startup, those tables may be created automatically when the backend starts successfully.

## 8. Create the Environment File

The backend uses environment variables to configure the PostgreSQL connection.

In the project root directory, create a file named exactly:

```text
.env
```

Place it beside `main.py`, `config.py`, and `requirements.txt`.

Add the following configuration:

```env
DB_CONNECTION=postgresql
POSTGRES_DB=furnova
POSTGRES_USERNAME=your_db_username
POSTGRES_PASSWORD=your_db_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

Replace the example username and password with the credentials for your local PostgreSQL user.

For example, if your local PostgreSQL user is `postgres`, use:

```env
POSTGRES_USERNAME=postgres
```

Use the actual password configured for that user.

### Important environment configuration notes

- `DB_CONNECTION` specifies the database type.
- `POSTGRES_DB` is the database name.
- `POSTGRES_USERNAME` is the PostgreSQL user.
- `POSTGRES_PASSWORD` is that user's password.
- `DB_HOST` is the PostgreSQL server address.
- `DB_PORT` is the PostgreSQL server port, normally `5432`.

The environment variable names must match the names read by the project's `config.py` or database configuration code.

**Never commit your real `.env` file or database password to GitHub.**

Make sure `.gitignore` contains:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
```

You can create a safe `.env.example` file to show teammates which settings are required without exposing real credentials:

```env
DB_CONNECTION=postgresql
POSTGRES_DB=furnova
POSTGRES_USERNAME=your_db_username
POSTGRES_PASSWORD=your_db_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

Commit `.env.example`, but keep your actual `.env` local.

## 9. Run the Application

Before starting the application, verify that:

- Your virtual environment is activated.
- All dependencies are installed.
- PostgreSQL is running.
- The `furnova` database exists.
- Your `.env` file contains the correct credentials.

Run the backend from the project root:

```powershell
python -m uvicorn main:app --reload
```

If startup succeeds, the terminal should show a message indicating that Uvicorn is running at:

```text
http://127.0.0.1:8000
```

The `--reload` option automatically restarts the server when you change your Python source files. It is intended for local development.

## 10. Verify the API

Open these URLs in your browser.

**API root**

http://127.0.0.1:8000/

Expected response:

```json
{
  "message": "Furnova API Running"
}
```

**Interactive API documentation**

http://127.0.0.1:8000/docs

**Alternative API documentation**

http://127.0.0.1:8000/redoc

If the API starts but database initialization fails, check the terminal output and confirm that your database settings match those in `config.py`.

## 11. Git Workflow for Contributors

After making changes, check your current branch:

```powershell
git branch --show-current
```

Make sure you are on your personal branch, not `main`.

Check the changed files:

```powershell
git status
```

Stage your changes:

```powershell
git add .
```

Commit your changes with a meaningful message:

```powershell
git commit -m "Add product model"
```

Replace the message with a short description of your actual changes.

Push your branch to your fork:

```powershell
git push -u origin your-name
```

If you already pushed the branch previously, you can normally use:

```powershell
git push
```

### Create a Pull Request

1. Open your personal fork on GitHub.
2. Select your personal branch.
3. Click **Contribute → Open pull request**, if available.
4. Set the base repository to `CCGP-Dev/Furniture_E-Com_Backend`.
5. Set the base branch to `main`.
6. Set the compare repository to your personal fork.
7. Select your personal branch as the compare branch.
8. Add a clear title and description.
9. Click **Create pull request**.

Wait for review and approval before merging.

### Keeping your branch up to date

Add the organization's repository as an upstream remote if it is not already configured:

```powershell
git remote add upstream https://github.com/CCGP-Dev/Furniture_E-Com_Backend.git
```

If `upstream` already exists, do not add it again.

Fetch the latest organization changes:

```powershell
git fetch upstream
```

Update your local `main`:

```powershell
git switch main
git pull upstream main
```

Update your own branch:

```powershell
git switch your-name
git merge main
```

If merge conflicts occur, resolve them before committing and pushing your branch.

## 12. Troubleshooting

### Error: `Could not import module "main"`

Make sure your terminal is in the project root, where `main.py` exists.

Run:

```powershell
python -c "import main"
```

Inspect the Python exception to identify the underlying import or configuration error.

### Error: PostgreSQL connection refused

Check that PostgreSQL is running and that `DB_HOST` and `DB_PORT` are correct.

### Error: Password authentication failed

Verify `POSTGRES_USERNAME` and `POSTGRES_PASSWORD` in your local `.env` file.

### Error: Database does not exist

Open pgAdmin and verify that the database named `furnova` exists on the same PostgreSQL server used by your application.

### Error: `ModuleNotFoundError`

Activate `.venv` and install dependencies again:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Error: Permission denied when pushing

Check that you are pushing to your personal fork, that you are authenticated to the correct GitHub account, and that you have the required repository permissions.

Verify your remotes:

```powershell
git remote -v
```

---

## Development Guidelines

- Never commit directly to `main`.
- Use a separate branch for each contributor or feature.
- Keep passwords, API keys, and other secrets out of Git.
- Do not commit `.venv` or generated Python cache files.
- Write meaningful commit messages.
- Test your changes before creating a Pull Request.
- Review your Pull Request and resolve conflicts before merging.

---

## Project Repository

**Organization:** CCGP-Dev

**Repository:** https://github.com/CCGP-Dev/Furniture_E-Com_Backend

**Technology stack:** Python, FastAPI, PostgreSQL, Git, and GitHub.

Happy coding! 🪑
