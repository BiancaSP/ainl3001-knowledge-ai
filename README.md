# AINL3001 — Knowledge-Driven AI

**TU850-3 BSc in Data Science and Artificial Intelligence**  
**Dr. Bianca Schoen-Phelan**  
**2026**

This repository contains the practical lab material for **AINL3001 — Knowledge-Driven AI**.

It contains:

- Weekly lab instructions
- Starter code
- Shared Python code
- Supporting resources
- Solution code when it is released

> **Important:** Open the entire `ainl3001-knowledge-ai` folder in VS Code rather than opening an individual week folder or Python file directly.

## Module Labs

| Week | Topic |
|---|---|
| 1 | [Problem Formulation](week01_problem_formulation/) |
| 2 | [Uninformed Search](week02_uninformed_search/) |
| 3 | [Informed Search](week03_informed_search/) |
| 4 | [Local Search and Optimisation](week04_local_search/) |
| 5 | [Constraint Satisfaction Problems](week05_csp/) |
| 6 | Adversarial Search |
| 7 | Logic |
| 8 | Knowledge Systems |
| 9 | Uncertainty |
| 10 | Planning |

Links for later weeks will be added as the relevant lab material is released.

## Repository Structure

The repository is organised by teaching week.

A simplified structure is:

```text id="c0fs55"
ainl3001-knowledge-ai/
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
│
├── common/
│   ├── __init__.py
│   ├── problem.py
│   └── grid_visualisation.py
│
├── week01_problem_formulation/
│   └── ...
│
├── week02_uninformed_search/
│   ├── README.md
│   ├── starter.py
│   └── solution.py
│
├── week03_informed_search/
│   ├── README.md
│   ├── starter.py
│   └── solution.py
│
└── week04_local_search/
    ├── README.md
    ├── tutorial_starter.py
    ├── queens_problem.py
    └── local_search_starter.py
```

Each weekly directory contains a `README.md` with the instructions for that week's lab.

The exact files may vary between weeks. Some labs use a single starter file, while others use several Python files.

Solutions may be released **after** the relevant lab rather than at the same time as the starter code.

## Shared Code

The `common/` directory contains Python code that can be reused across different labs.

For example:

```python id="fx4ug2"
from common.problem import Problem
```

or:

```python id="yop12a"
from common.grid_visualisation import show_final_path
```

From Week 4 onwards, we will begin using shared representations where appropriate.

Earlier labs intentionally use more direct problem representations. This allows us to see how our code develops as we introduce more AI techniques.

# Getting Started

## 1. Fork the Module Repository

Do **not** use the module repository itself as the repository for your lab work.

First, create your own copy using GitHub's **Fork** button.

The module repository is:

```text id="0lm1dn"
https://github.com/BiancaSP/ainl3001-knowledge-ai
```

Your fork will appear under your own GitHub account.

For example:

```text id="l9avk1"
https://github.com/<your-username>/ainl3001-knowledge-ai
```

Your fork is where you will push your lab work.

## 2. Choose a Local Folder

Do **not** store your active Git repository inside OneDrive or another cloud-synchronised directory.

For example, avoid:

```text id="d3rtbs"
OneDrive/
OneDrive - TU Dublin/
```

Also avoid `Documents` or `Desktop` if those directories are being synchronised by OneDrive.

Instead, use a normal local directory such as:

### Windows

```text id="3nb6y9"
C:\Users\YourName\GitHub\
```

or:

```text id="0rhhw5"
C:\Users\YourName\Projects\
```

### macOS / Linux

```text id="mfr8bi"
~/GitHub/
```

or:

```text id="oua37r"
~/Projects/
```

Use **GitHub**, rather than OneDrive, to synchronise your Git repository between computers.

## 3. Clone Your Fork

Clone **your own fork**, not the module repository.

On your GitHub fork, click **Code** and copy its HTTPS address.

Then run:

```bash id="mqmn8k"
git clone https://github.com/<your-username>/ainl3001-knowledge-ai.git
```

Move into the repository:

```bash id="hn71zx"
cd ainl3001-knowledge-ai
```

## 4. Check `origin`

When you clone your fork, Git automatically creates a remote called `origin`.

Check it with:

```bash id="js52j4"
git remote -v
```

`origin` should point to **your GitHub repository**.

For example:

```text id="vrm4dw"
origin  https://github.com/<your-username>/ainl3001-knowledge-ai.git (fetch)
origin  https://github.com/<your-username>/ainl3001-knowledge-ai.git (push)
```

## 5. Add the Module Repository as `upstream`

The module repository will be used to distribute new teaching material.

Add it as a remote called `upstream`:

```bash id="2x4gh8"
git remote add upstream https://github.com/BiancaSP/ainl3001-knowledge-ai.git
```

Check your remotes again:

```bash id="x7bx4d"
git remote -v
```

You should now have:

```text id="xjuxqv"
origin    → your GitHub repository
upstream  → the module GitHub repository
```

A useful rule to remember is:

> **Get teaching material from `upstream`. Push your work to `origin`.**

# Python Setup

The repository contains a small amount of shared Python code and some external Python dependencies.

Complete the following setup from the **top-level repository directory**.

You normally only need to do this once per computer or Python environment.

## 1. Install the Requirements

On macOS/Linux:

```bash id="txdix3"
python3 -m pip install -r requirements.txt
```

If your Python installation uses `python` rather than `python3`, use:

```bash id="a87p6n"
python -m pip install -r requirements.txt
```

## 2. Install the Shared Code

Next run:

```bash id="uh1axm"
python3 -m pip install -e .
```

or:

```bash id="1l9t0k"
python -m pip install -e .
```

The final `.` means the project in the **current directory**.

The `-e` means **editable install**.

This allows weekly lab files to import shared code such as:

```python id="wy1n3c"
from common.problem import Problem
```

without copying the shared code into every weekly directory.

## 3. `ainl3001.egg-info`

After running:

```bash id="o4c3dn"
python3 -m pip install -e .
```

you may notice a new directory:

```text id="m0w3hz"
ainl3001.egg-info/
```

This is **normal**.

It is automatically generated by Python's packaging tools.

You do not need to open, edit, delete, commit, or push this directory.

The repository's `.gitignore` tells Git to ignore generated files such as:

```text id="w3g7mm"
*.egg-info/
__pycache__/
*.pyc
```

Therefore, `ainl3001.egg-info/` may exist on your computer without being included in your Git commits.

# Using VS Code

Open the **entire repository** in VS Code.

Select:

**File → Open Folder**

and choose:

```text id="1nploa"
ainl3001-knowledge-ai
```

Do not open only an individual week directory.

Do not work by opening individual Python files outside the repository.

Opening the complete repository makes it easier to:

- See the full project structure.
- Work with the weekly lab files.
- Use shared code from `common/`.
- Use Git and Source Control.
- Run Python files using the correct project structure.

After completing the Python setup, you can normally run the current Python file using VS Code's **Run Python File** button.

# Testing the Shared Python Code

You can check that the shared code is installed correctly by running this from the repository root:

```bash id="oj4cr4"
python3 -c "from common.problem import Problem; print('Import works')"
```

or:

```bash id="mhxpj5"
python -c "from common.problem import Problem; print('Import works')"
```

You should see:

```text id="y2p8p2"
Import works
```

If you see:

```text id="lknj1a"
ModuleNotFoundError: No module named 'common'
```

make sure you are in the top-level `ainl3001-knowledge-ai` directory and run:

```bash id="8mqy0v"
python3 -m pip install -e .
```

If the import works in the terminal but not when using **Run Python File** in VS Code, use:

**View → Command Palette → Python: Select Interpreter**

and make sure VS Code is using the same Python installation in which you installed the project.


# Working on a Lab

Open the directory for the relevant week.

For example:

```text id="bklqyc"
week04_local_search/
```

Read that directory's:

```text id="6jx1gj"
README.md
```

before beginning.

The weekly README contains the detailed instructions, tasks, experiments, reflection questions, and any extension activities for that lab.

Where starter files are supplied, **modify the starter files directly unless the lab instructions say otherwise**.

Do not rename the starter files simply to create your solution. Git records the development of your files through commits.

# Committing Your Work

Commit your work regularly as you complete meaningful parts of a lab.

Check what has changed:

```bash id="0rtchh"
git status
```

Stage a file:

```bash id="l9t16g"
git add <file>
```

Commit it:

```bash id="8k5yb6"
git commit -m "Describe what you changed"
```

For example:

```bash id="crq0zu"
git add week04_local_search/local_search_starter.py
git commit -m "Implemented conflict function"
```

Then push your commits to your GitHub repository:

```bash id="t8ayyy"
git push
```

A useful way to think about the process is:

```text id="mx1zhb"
EDIT
 ↓
git status
 ↓
git add
 ↓
git commit
 ↓
git push
```

A **commit** records your work locally.

A **push** sends your commits to your GitHub repository.

# Getting New Lab Material

Do not clone the repository again each week.

Your repository should develop throughout the module.

At the start of a new lab, first check:

```bash id="96gt0d"
git status
```

Make sure your existing work has been committed.

Then retrieve the latest module material:

```bash id="qfnz2g"
git fetch upstream
```

Merge it into your local `main` branch:

```bash id="9i4d3e"
git merge upstream/main
```

Then update your own GitHub repository:

```bash id="8i9p9j"
git push origin main
```

The normal flow is:

```text id="3prl1f"
MODULE REPOSITORY
    upstream
       ↓
     fetch
       ↓
     merge
       ↓
LOCAL REPOSITORY
       ↓
      work
       ↓
     commit
       ↓
      push
       ↓
YOUR GITHUB REPOSITORY
     origin
```

# `origin` and `upstream`

Remember the distinction:

| Remote | Repository | Purpose |
|---|---|---|
| `origin` | Your GitHub repository | Store and synchronise your work |
| `upstream` | Module GitHub repository | Receive new teaching material |

Therefore:

```text id="44p1da"
upstream
   ↓
new module material
   ↓
your local repository
   ↓
your work and commits
   ↓
origin
```

You should **not push your lab work to `upstream`**.

# Working on More Than One Computer

If you work on another computer, clone your own GitHub repository onto that computer.

Do not copy the active repository using OneDrive.

On the second computer:

```bash id="j9xxbu"
git clone https://github.com/<your-username>/ainl3001-knowledge-ai.git
cd ainl3001-knowledge-ai
```

Add the module repository:

```bash id="67vlhf"
git remote add upstream https://github.com/BiancaSP/ainl3001-knowledge-ai.git
```

Install the Python requirements and shared code:

```bash id="l2d0cv"
python3 -m pip install -r requirements.txt
python3 -m pip install -e .
```

Use `python` instead of `python3` if required by your Python installation.

Before moving from one computer to another, make sure you have committed and pushed your work.

On the other computer, use:

```bash id="8wd8e7"
git pull
```

to retrieve your latest work.


# Quick Reference

## First-Time Setup

```text id="cjxk4b"
FORK
  ↓
CLONE YOUR FORK
  ↓
ADD UPSTREAM
  ↓
INSTALL REQUIREMENTS
  ↓
INSTALL SHARED CODE
  ↓
OPEN REPOSITORY IN VS CODE
```

## Start of a New Lab

```bash id="3vkv2k"
git status
git fetch upstream
git merge upstream/main
git push origin main
```

## While Working

```bash id="zhykrv"
git status
git add <file>
git commit -m "Describe what you changed"
git push
```

## Remember

- Read the `README.md` inside each week's directory.
- Work directly in the supplied starter files unless instructed otherwise.
- Open the entire repository in VS Code.
- Keep the active Git repository outside OneDrive.
- Commit your work regularly.
- Push your work to **your repository (`origin`)**.
- Get new module material from **the module repository (`upstream`)**.
- Do not worry if `ainl3001.egg-info/` appears after installing the project — Git will ignore it.
- Solutions may be released later and will become available when you update from `upstream`.