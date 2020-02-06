import re
from ast import Module

from flake8_plugin.analyzer import DjangoModelAnalyzer


class DjangoModelDocString:
    """Flake8 plugin that's checks documentation for django models.

    Attributes:
        name (str): Name of plugin
        version (str): Version of plugin
        model_filepath_pattern (str):
            Regex rule for matching possible location of models classes

    """
    model_filepath_pattern: str = (
        r'(apps/)?[a-z_]+/(models.py|models/[a-z_]*.py)'
    )
    name: str = 'flake8-django-docstrings'
    version: str = '0.0.1'

    def __init__(self, tree, filename):
        """Init plugin.

        Attributes:
            tree: Node of file in python ast module
            filename (str): Location of file, that will be checked

        """
        self.tree: Module = tree
        self.filename: str = filename

    def run(self):
        """Run plugin against file.

        First we check if file is related to django models, if not we skip
        checking. If file is related to to django models we initiate analyzer
        run it against tree of file and yield one by one unpacked issues.

        """
        if not self.is_model_file():
            return

        analyzer = DjangoModelAnalyzer()
        analyzer.visit(self.tree)

        for issue in analyzer.issues:
            yield issue.lineno, issue.col, issue.message, DjangoModelDocString

    def is_model_file(self) -> bool:
        """Check if incoming file is related to django models or not."""
        return bool(re.search(
            pattern=self.model_filepath_pattern,
            string=self.filename
        ))
