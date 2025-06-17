# FoxLab Cookiecutter

Cookiecutter repo for generating python projects.

## Usage

Make sure the `cookiecutter` package is installed:

```bash
pip install cookiecutter
```

Next, install the template directly from this repo:

```bash
cookiecutter https://github.com/foxlab-ucdavis/foxlab-cookie.git
```

Finally, install the environment and dependencies:

```bash
make install
```

If you have added a new dependency, make sure to update the `requirements.txt` file:

```bash
make update
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
└── <project_name>/        # your git repo
    ├── data  -> ../data
    ├── models -> ../models
    ├── reports -> ../reports
    └── ... project code ...
```

The symlinks under `<project_name>/` give your code convenient relative paths while keeping large artefacts out of version control.

When you run `cookiecutter https://github.com/foxlab-ucdavis/foxlab-cookie.git`, you will be prompted for `workspace_name` first, followed by the usual project details.
