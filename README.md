![Build](https://github.com/TheSuperiorStanislav/flake-django-models-docs/workflows/Build/badge.svg?branch=feature%2Fgithub-action)
# Flake 8 plugin that checks docstrings for Django models

It will show code style errors in this cases:
* Model class doesn't have docstring at all
* Model class's docstring doesn't describes model's fields
* Model class's proprieties doesn't have docstrings

## Error codes:

* `DMD1` - Model class doesn't have docstring at all
* `DMD2` - Model class's docstring doesn't describes model's fields. They should be described 
like this: `field_name` (`type`): `description`
* `DMD3` - Model class's proprieties doesn't have docstrings

## Developing 

First you need to install all needed dependencies for development:
```
pip install -r development.txt 
```

To install plugin into your current environment:
```
pip install .
```

If you are working with PyCharm, this plugin might be useful [pytest-pycharm](https://github.com/jlubcke/pytest-pycharm)

To fully check your code with style check run this:
```
pytest --isort --flake8
```

To just fo style check run this:
```
pytest --isort --flake8 -m "isort or flake8"
```

To test your code against different versions of python run:
```
tox
```
*Note: they must be `installed`(you can do it by `pyenv`)*

If want ot specify version of python:
```
tox -e py35
```
To run in parallel:
```
tox --parallel auto
```
