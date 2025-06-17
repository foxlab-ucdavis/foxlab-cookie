# FoxLab Cookiecutter

Cookiecutter repo for generating python projects. The lab-specific template is designed to scaffold a project with a clean structure, using `uv` for dependency management and virtual environments.

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
    ├── docs            # documentation (e.g., tutorials, usage guides, etc)
    └── project_name/   # your actual project source code
```

The symlinks under `<project_name>/` give your code convenient relative paths while keeping large artefacts out of version control.

When you run `cookiecutter https://github.com/foxlab-ucdavis/foxlab-cookie.git`, you will be prompted for `workspace_name` first, followed by the usual project details.

## Installation

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

## Basic Usage

When you need to add additional dependencies to your project, you can do so using:

```bash
uv add <dependency>
```

This will automatically add the dependency to the `pyproject.toml` file, update the `uv.lock` lock file, and install the new dependency in the virtual environment.

To generate a `requirements.txt` file (e.g., when sharing your project with someone who does not use `uv`), you can run:

```bash
make requirements
```

> [!NOTE] Specifying Python Version
> By default, this template uses python 3.12. If this does not suit your needs, you can change your Python version by doing the following:
>
> 1. Update the `requires-python` field in `pyproject.toml`
> 2. Update the `make install` command in the `Makefile` to use the desired Python version, e.g., `uv sync --python 3.11`
> 3. Reinstall dependencies with: `make install` or `uv sync --python 3.11`
>
> Thanks to `uv`'s built-in Python management, missing interpreters will be automatically downloaded when needed.
