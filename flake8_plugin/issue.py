class Issue(object):
    """Base class for flake8 issues."""
    code = None
    description = None

    def __init__(self, lineno, col, **extra_data):
        self.extra_data = extra_data
        self.col = col
        self.lineno = lineno

    @property
    def message(self):
        """Return issue message, which will be display to user"""
        message = self.description.format(**self.extra_data)
        return '{code} {message}'.format(code=self.code, message=message)


class DMD1(Issue):
    """Class for flake8 issue(when model doesn't have docs at all)."""
    code = 'DMD1'
    description = 'Class `{model_name}` must have docs'


class DMD2(Issue):
    """Class for flake8 issue(when model doesn't have docs for field)."""
    code = 'DMD2'
    description = 'Class `{model_name}` must have docs for `{field}`'


class DMD3(Issue):
    """Class for flake8 issue(when model property doesn't have docs)."""
    code = 'DMD3'
    description = (
        'Class `{model_name}` must have docs for property `{property}`'
    )