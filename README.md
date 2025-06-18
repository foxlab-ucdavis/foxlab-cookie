# FoxLab Cookiecutter

Cookiecutter repo for generating python projects. The lab-specific template is designed to scaffold a project with a clean structure, using `uv` for dependency management and virtual environments.

This template uses a workspace-first approach where you create your workspace directory first, then run cookiecutter from within it to generate your project.

## Intended Structure

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

## Quick Start

1. **Create your workspace directory:**

   ```bash
   mkdir my-research-workspace
   cd my-research-workspace
   ```

2. **Generate your project:**

   ```bash
   cookiecutter https://github.com/foxlab-ucdavis/foxlab-cookie.git
   ```

3. **Answer the prompts:**
   - `project_name`: Name of your project (e.g., `awesome-analysis`)
   - `create_models_directory`: Choose `y` if you need a models folder
   - `create_symlinks`: Choose `y` to create shared workspace directories
   - Other standard project details

> [!NOTE] Updating cookiecutter template
> If you want to update your project with the latest changes from the template, you can run:
>
> ```bash
> cookiecutter https://github.com/foxlab-ucdavis/foxlab-cookie.git --replay
> ```
>
> And follow the prompt to delete and re-download the template.

### Symlinks

When you choose `create_symlinks: y`, the template automatically:

1. **Creates shared directories** in your workspace (`../data`, `../reports`, `../models`) **only if they don't already exist** - existing directories and their contents are preserved
2. **Creates symlinks** from your project to these directories
3. **Keeps large files out of git** while giving your code convenient relative paths

This means you can:

- Share datasets between multiple projects in the same workspace
- Keep your git repositories lightweight
- Use simple relative paths like `./data/raw/dataset.csv` in your code
- Organize multiple related projects under one workspace

### Multiple Projects in One Workspace

You can generate multiple projects in the same workspace:

```bash
cd my-research-workspace
cookiecutter https://github.com/foxlab-ucdavis/foxlab-cookie.git  # Creates project-1
cookiecutter https://github.com/foxlab-ucdavis/foxlab-cookie.git  # Creates project-2
```

Both projects will share the same `data/`, `models/`, and `reports/` directories through symlinks.

## Installation

If you have `uv` installed, you can install cookiecutter as a tool using:

```bash
uv tool install cookiecutter
```

Next, install the template directly from this repo:

```bash
cookiecutter https://github.com/foxlab-ucdavis/foxlab-cookie.git
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
