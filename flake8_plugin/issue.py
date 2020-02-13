class Issue(object):
    """Base class for flake8 issues.

    Attributes:
        code (str):
            Identifier of issue for flake8, can be used in config to ignore it
        message_template (str):
            Template of message which will be showed to user
        extra_data (dict):
            Extra payload which will be used in template rendering
        lineno (int): Line where issue was found
        col (int): Column where issue was found

    """
    code = None
    message_template = None

    def __init__(self, lineno: int, col: int, **extra_data):
        """Initialize the issue."""
        self.extra_data = extra_data
        self.col = col
        self.lineno = lineno

    @property
    def message(self):
        """Return issue message, which will be displayed to user."""
        message = self.message_template.format(**self.extra_data)
        return '{code} {message}'.format(code=self.code, message=message)

    def __repr__(self):
        """Representation of issue for debugging purposes."""
        return (
            "code={code}, "
            "col={col}, lineno={self.lineno}, "
            "model_name='{model_name}', "
            "message={message}"
        ).format(
            code=self.code,
            lineno=self.lineno,
            col=self.col,
            model_name=self.extra_data['model_name'],
            message=self.message
        )


class DMD1(Issue):
    """Class for flake8 issue(when model doesn't have docs at all)."""
    code = 'DMD1'
    message_template = 'Model `{model_name}` must have docs'


class DMD2(Issue):
    """Class for flake8 issue(when model doesn't have docs for field)."""
    code = 'DMD2'
    message_template = 'Model `{model_name}` must have docs for `{field}`'


class DMD3(Issue):
    """Class for flake8 issue(when model property doesn't have docs)."""
    code = 'DMD3'
    message_template = (
        'Model `{model_name}` must have docs for property `{property}`'
    )
