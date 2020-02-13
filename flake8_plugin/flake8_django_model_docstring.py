import re
from collections import namedtuple

from flake8_plugin.analyzer import DjangoModelAnalyzer
from flake8_plugin.issue import Issue

FlakeIssue = namedtuple(
    'FlakeIssue', ('lineno', 'col', 'message', 'plugin_class')
)


class DjangoModelDocString:
    """Flake8 plugin that's checks documentation for django models.

    Attributes:
        name (str): Name of plugin
        version (str): Version of plugin
        model_filepath_pattern (str):
            Regex rule for matching possible location of models classes

    """
    model_filepath_pattern = (
        r'(apps/)?[a-z_]+/(models.py|models/[a-z_]*.py)'
    )
    name = 'flake8-django-docstrings'
    version = '0.0.1'

    def __init__(self, tree, filename: str):
        """Init plugin.

        Attributes:
            tree: Node of file in python ast module
            filename (str): Location of file, that will be checked

        """
        self.tree = tree
        self.filename = filename

    def run(self):
        """Run plugin against file.

        First we check if file is related to django models, if not we skip
        checking. If file is related to django models we initiate analyzer to
        run it against tree of file and yield one by one unpacked issues.

        """
        if not self.is_model_file():
            return

        analyzer = DjangoModelAnalyzer()
        analyzer.visit(self.tree)

        for issue in analyzer.issues:
            yield self.flake_issue(issue)

    def is_model_file(self) -> bool:
        """Check if incoming file is related to django models or not."""
        return bool(re.search(
            pattern=self.model_filepath_pattern,
            string=self.filename
        ))

    def flake_issue(self, issue: Issue) -> FlakeIssue:
        return FlakeIssue(
            lineno=issue.lineno,
            col=issue.col,
            message=issue.message,
            plugin_class=self.__class__
        )
