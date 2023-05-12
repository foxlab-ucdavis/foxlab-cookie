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
