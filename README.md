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