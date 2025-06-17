#!/usr/bin/env python
import os
import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()
REPO_NAME = "{{cookiecutter.project_name}}"
REPO_DIRECTORY = PROJECT_DIRECTORY / REPO_NAME


def remove(filename: str) -> None:
    filepath = next(PROJECT_DIRECTORY.rglob(f"{filename}"))
    if filepath.is_file():
        filepath.unlink()
    elif filepath.is_dir():
        shutil.rmtree(filepath)


def ensure_symlink(name: str) -> None:
    """Create a relative symlink inside the repo pointing to the workspace folder."""
    src = PROJECT_DIRECTORY / name  # e.g. ../data
    dest = REPO_DIRECTORY / name
    if dest.exists() or dest.is_symlink():
        return
    try:
        # Use a relative path so the repo can be moved around inside workspace
        rel_src = os.path.relpath(src, dest.parent)
        dest.symlink_to(rel_src, target_is_directory=True)
    except OSError:
        # On Windows, symlink may require admin; fall back to creating a directory junction
        shutil.copytree(src, dest, dirs_exist_ok=True)


if __name__ == "__main__":
    if "{{cookiecutter.create_models_directory}}" != "y":
        remove("models")
    # create symlinks inside the repo so that code can refer to data/ etc.
    for artefact in ["data", "reports", "models"]:
        # Skip models if it was just removed
        if artefact == "models" and "{{cookiecutter.create_models_directory}}" != "y":
            continue
        ensure_symlink(artefact)
