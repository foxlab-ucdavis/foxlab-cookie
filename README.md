# FoxLab Cookiecutter

Cookiecutter repo for generating python projects.

## Usage

### Installation

If you have `uv` installed, you can install cookiecutter as a tool using:

```bash
uv tool install cookiecutter
```

Next, install the template directly from this repo:

```bash
uv tool run cookiecutter https://github.com/foxlab-ucdavis/foxlab-cookie.git
# note: `uvx` is simply shorthand for `uv tool run`
uvx cookiecutter https://github.com/foxlab-ucdavis/foxlab-cookie.git
```

To install the environment and dependencies run:

```bash
make install
```

### Basic Usage

When you need to add additional dependencies to your project, you can do so using:

```bash
uv add <dependency>
```

This will automatically add the dependency to the `pyproject.toml` file, update the `uv.lock` lock file, and install the new dependency in the virtual environment.

To generate a `requirements.txt` file (e.g., when sharing your project with someone who does not use `uv`), you can run:

```bash
make requirements
```

## Initial modifications

It is a good idea to make the following changes to the project after it is generated:

- Update the cookiecutter.json file with your information. To do this, navigate to the `.cookiecutters` folder in your home directory and open the `cookiecutter.json` file. Update the `author`, `email`, `author_github_handle` fields. This way, the next time you generate a project, these fields will be automatically filled in.

## Generated Project Layout (v2)

The template now scaffolds a *workspace* directory that sits **outside** the git repository.  Your answers to the prompts create two independent names:

1. `workspace_name` – top-level folder that holds large, non-versioned artefacts (defaults to `new-workspace`).
2. `project_name` – folder that becomes the git repository (what you push to GitHub).

After generation the structure looks like:

```text
<workspace_name>/
├── data/                  # raw / interim / processed datasets (not committed)
├── models/                # model checkpoints (optional)
├── reports/               # generated reports / figures
└── <project-name>/        # your git repo
    ├── data     ->      ../data
    ├── models   ->     ../models
    ├── reports  ->    ../reports
    ├── notebooks       # Jupyter notebooks (optional)
    └── project_name/   # your actual project source code
```

The symlinks under `<project_name>/` give your code convenient relative paths while keeping large artefacts out of version control.

When you run `cookiecutter https://github.com/foxlab-ucdavis/foxlab-cookie.git`, you will be prompted for `workspace_name` first, followed by the usual project details.
