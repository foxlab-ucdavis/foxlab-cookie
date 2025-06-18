#!/usr/bin/env python
import os
import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def remove(filename: str) -> None:
    """Remove a file or directory from the generated project."""
    try:
        filepath = next(PROJECT_DIRECTORY.rglob(f"{filename}"))
        if filepath.is_file():
            filepath.unlink()
        elif filepath.is_dir():
            shutil.rmtree(filepath)
    except StopIteration:
        pass


def create_workspace_directories(include_models: bool = False) -> None:
    """Create data, models, and reports directories in the parent workspace if they don't exist."""
    parent_dir = PROJECT_DIRECTORY.parent
    data_dir = parent_dir / "data"
    data_dir.mkdir(exist_ok=True)
    reports_dir = parent_dir / "reports"
    reports_dir.mkdir(exist_ok=True)

    if include_models:
        models_dir = parent_dir / "models"
        models_dir.mkdir(exist_ok=True)


def create_symlink(name: str) -> None:
    """Create a relative symlink inside the project pointing to the workspace folder."""
    src = PROJECT_DIRECTORY.parent / name  # e.g. ../data
    dest = PROJECT_DIRECTORY / name

    if dest.exists() or dest.is_symlink():
        if dest.is_symlink():
            dest.unlink()
        elif dest.is_dir():
            shutil.rmtree(dest)
        elif dest.is_file():
            dest.unlink()

    try:
        rel_src = os.path.relpath(src, dest.parent)
        dest.symlink_to(rel_src, target_is_directory=True)
        print(f"Created symlink: {name} -> {rel_src}")
    except OSError as e:
        print(f"Warning: Could not create symlink for {name}: {e}")
        # On Windows or if symlinks aren't supported, just ensure the directory exists
        dest.mkdir(exist_ok=True)


if __name__ == "__main__":
    include_models = "{{cookiecutter.create_models_directory}}" == "y"
    include_notebooks = "{{cookiecutter.create_notebook_directory}}" == "y"

    if not include_models:
        remove("models")

    if not include_notebooks:
        remove("notebooks")

    if "{{cookiecutter.create_symlinks}}" == "y":
        print("Creating workspace directories and symlinks...")

        create_workspace_directories(include_models=include_models)

        create_symlink("data")
        create_symlink("reports")

        if include_models:
            create_symlink("models")

        print("Workspace setup complete!")
        print(f"Your project is ready at: {PROJECT_DIRECTORY}")
        print("Shared directories created:")
        print(f"  - {PROJECT_DIRECTORY.parent}/data")
        print(f"  - {PROJECT_DIRECTORY.parent}/reports")
        if include_models:
            print(f"  - {PROJECT_DIRECTORY.parent}/models")
        if include_notebooks:
            print(f"  - {PROJECT_DIRECTORY.parent}/notebooks")
    else:
        print("Skipped creating symlinks to shared workspace directories.")
        print(f"Your project is ready at: {PROJECT_DIRECTORY}")
