import sys
from ast import parse
from collections import namedtuple

import pytest
from flake8_plugin import DjangoModelDocString, issue
from flake8_plugin.analyzer import DjangoModelAnalyzer
from packaging import version

IssueResults = namedtuple(
    'IssueResults', ('col', 'lineno', 'model_name')
)
BASE_PATH = 'tests/fixtures/'
CURRENT_VERSION = version.parse('{major}.{minor}.{micro}'.format(
    major=sys.version_info.major,
    minor=sys.version_info.minor,
    micro=sys.version_info.micro
))


def create_file_tree(filename: str):
    """Create tree of test file"""
    with open(filename, 'r') as source:
        tree = parse(source.read())
    return tree


def test_issue_discovery():
    """Check that analyzer finds issues in correct spots."""
    filename = '{BASE_PATH}app_with_models_module/models.py'.format(
        BASE_PATH=BASE_PATH
    )
    analyzer = DjangoModelAnalyzer()
    analyzer.visit(create_file_tree(filename))
    issues_types = (
        (
            issue.DMD1,
            IssueResults(col=0, lineno=9, model_name='ModelWithDMD1')
        ),
        (
            issue.DMD2,
            IssueResults(col=4, lineno=21, model_name='ModelWithDMD2')
        ),
        (
            issue.DMD3,
            IssueResults(col=0, lineno=36, model_name='ModelWithDMD3')
        )
    )
    for issue_type, issue_data in issues_types:
        issues = tuple(
            filter(lambda x: isinstance(x, issue_type), analyzer.issues)
        )
        assert issues
        assert len(issues) == 1
        found_issue = issues[0]

        assert found_issue.col == issue_data.col
        # Python 3.8 and higher discover properties at one line lower
        if issue_type == issue.DMD3:
            if CURRENT_VERSION >= version.parse('3.8.0'):
                assert found_issue.lineno == issue_data.lineno
            else:
                assert found_issue.lineno == issue_data.lineno - 1
        else:
            assert found_issue.lineno == issue_data.lineno
        assert found_issue.extra_data['model_name'] == issue_data.model_name


test_files_paths = (
    (
        '{path}app_with_models_module/models.py'.format(
            path=BASE_PATH
        ), 3
    ),
    (
        '{path}app_with_models_package/models/foo.py'.format(
            path=BASE_PATH
        ), 3
    ),
    (
        '{path}apps/app_with_models_module/models.py'.format(
            path=BASE_PATH
        ), 3
    ),
    (
        '{path}apps/app_with_models_package/models/correct_file.py'.format(
            path=BASE_PATH
        ), 0
    ),
    (
        '{path}app_with_models_package/models/correct_file.py'.format(
            path=BASE_PATH
        ), 0
    ),
    (
        '{path}app_with_models_module/forms.py'.format(
            path=BASE_PATH
        ), 0
    ),
)


@pytest.mark.parametrize(
    'filename, issue_count, ',
    test_files_paths
)
def test_file_checking(filename: str, issue_count: int):
    """Check that plugin correctly identifies files and returns errors."""
    plugin = DjangoModelDocString(
        tree=create_file_tree(filename), filename=filename
    )
    issues = tuple(plugin.run())
    assert len(issues) == issue_count
