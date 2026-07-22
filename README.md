# Causal Inference Demo: Collider Bias

This repository contains a small simulation to demonstrate collider bias in causal inference.

## Files

- `explore_collider.py`: Simulates independent variables `talent` and `beauty`, creates a collider (`is_celebrity`), and compares regression estimates with and without conditioning on the collider.
- `requirements.txt`: Lists the Python dependencies needed to run the script.

## Setup

1. Create or activate your virtual environment.
2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Virtual environment (recommended)

This project uses a Python virtual environment, which is an isolated Python setup just for this folder.
It keeps the package versions for this project separate from other Python work on your computer.

### Why use a virtual environment?

- avoids conflicts between projects
- keeps dependencies reproducible
- lets you install packages safely without changing global Python

### Create the virtual environment

Run this once in the project folder:

```powershell
python -m venv .venv
```

### Activate the virtual environment

Then activate it before installing packages or running the script.

On Windows PowerShell:

```powershell
.\.venv\Scripts\activate
```

On Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

Once activated, your prompt should show `(.venv)`.

### Install dependencies

With the environment active, install packages from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

### Launch the Jupyter notebook

After dependencies are installed, start Jupyter Notebook from this folder:

```powershell
python -m notebook
```

Then open `explore_collider.ipynb` in the browser.

In the notebook, run the first code cell to import libraries, then run the cells that simulate data and display the regression results and plots.

If you are using VS Code, you can also open `explore_collider.ipynb` directly and use the built-in notebook interface.

### Notebook troubleshooting

If Jupyter does not start or the notebook does not run:

- Make sure the virtual environment is activated: `.\.venv\Scripts\activate`
- Make sure dependencies are installed: `python -m pip install -r requirements.txt`
- Close and reopen VS Code if the notebook kernel is not detected.
- If you still see errors, run the notebook from the command line and check the output for the missing package or path issue.

### Use the environment in VS Code

VS Code can automatically use the project environment if you select the interpreter from `.venv`.

1. Open the Command Palette with `Ctrl+Shift+P`.
2. Choose `Python: Select Interpreter`.
3. Pick the interpreter at:
   `.venv\Scripts\python.exe`

This ensures the code runs with the same packages installed in this project.

### Automatic VS Code setting

This workspace already includes `.vscode/settings.json` with the correct interpreter path:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe"
}
```

That makes VS Code automatically pick the right environment for this project.

## Run

```bash
python DAG.py
```

## Using GitHub Desktop

If you prefer to use GitHub Desktop to push and sync this repository, follow these steps:

1. Open GitHub Desktop.
2. File → **Add local repository...** → select this project folder and click **Add Repository**.
3. In the **Changes** tab, review your files. Enter a commit message (e.g., "Add README and code") and click **Commit to main** (or **Commit to master**).
4. To publish the repository to GitHub, click **Publish repository** in the top bar, choose the owner and repository name, then click **Publish repository**.
  - If you already created an empty repository on GitHub.com, instead click **Repository → Repository settings → Remote**, then **Add remote** and paste the remote URL (for example `https://github.com/username/repo.git`). After adding the remote, use **Push origin** to upload commits.
5. For subsequent changes: make commits in GitHub Desktop and click **Push origin** to sync to GitHub.

If you prefer the command line, you can push with:

```bash
git remote add origin <REMOTE_URL>
git branch -M main
git push -u origin main
```

Note: GitHub Desktop may open your browser to authenticate. Make sure you're signed into the correct GitHub account.

## What it shows

- `Analysis 1`: Regression of `talent` on `beauty` in the full population.
- `Analysis 2`: Regression of `talent` on `beauty` among celebrities only, which conditions on the collider.

This demonstrates how conditioning on a collider can induce a spurious association between otherwise independent variables.

## Example output

When you run `python DAG.py`, you should see output like:

```text
Analysis 1: General Population (Unconditioned)
Estimated Coefficient for Beauty: 0.0000
P-value for Beauty: 0.9990

Analysis 2: Conditioned on Celebrity Status (Collider)
Estimated Coefficient for Beauty: -0.2300
P-value for Beauty: 0.0000
```

The exact values will vary slightly due to random sampling, but the key point is that the collider-conditioned model shows a strong spurious association.
