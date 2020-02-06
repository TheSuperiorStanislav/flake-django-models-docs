from ast import parse
from collections import namedtuple

import pytest

from flake8_plugin import issue
from flake8_plugin.analyzer import DjangoModelAnalyzer


def create_file_tree(filename: str):
    with open(filename, 'r') as source:
        tree = parse(source.read())
    return tree


IssueResults = namedtuple(
    'IssueResults', ('col', 'lineno', 'model_name')
)

test_params = (
    (
        'tests/app_with_models_module/models.py',
        issue.DMD1,
        IssueResults(col=0, lineno=9, model_name='ModelWithDMD1')
    ),
    (
        'tests/app_with_models_package/models/foo.py',
        issue.DMD1,
        IssueResults(col=0, lineno=9, model_name='ModelWithDMD1')
    ),
    (
        'tests/apps/app_with_models_module/models.py',
        issue.DMD1,
        IssueResults(col=0, lineno=9, model_name='ModelWithDMD1')
    ),
    (
        'tests/apps/app_with_models_package/models/foo.py',
        issue.DMD1,
        IssueResults(col=0, lineno=9, model_name='ModelWithDMD1')
    ),
    (
        'tests/app_with_models_module/models.py',
        issue.DMD2,
        IssueResults(col=4, lineno=21, model_name='ModelWithDMD2')
    ),
    (
        'tests/app_with_models_package/models/foo.py',
        issue.DMD2,
        IssueResults(col=4, lineno=21, model_name='ModelWithDMD2')
    ),
    (
        'tests/apps/app_with_models_module/models.py',
        issue.DMD2,
        IssueResults(col=4, lineno=21, model_name='ModelWithDMD2')
    ),
    (
        'tests/apps/app_with_models_package/models/foo.py',
        issue.DMD2,
        IssueResults(col=4, lineno=21, model_name='ModelWithDMD2')
    ),
    (
        'tests/app_with_models_module/models.py',
        issue.DMD3,
        IssueResults(col=0, lineno=36, model_name='ModelWithDMD3')
    ),
    (
        'tests/app_with_models_package/models/foo.py',
        issue.DMD3,
        IssueResults(col=0, lineno=36, model_name='ModelWithDMD3')
    ),
    (
        'tests/apps/app_with_models_module/models.py',
        issue.DMD3,
        IssueResults(col=0, lineno=36, model_name='ModelWithDMD3')
    ),
    (
        'tests/apps/app_with_models_package/models/foo.py',
        issue.DMD3,
        IssueResults(col=0, lineno=36, model_name='ModelWithDMD3')
    ),
)


@pytest.mark.parametrize(
    'filename, issue_type, issue_data',
    test_params
)
def test_issue_discovery(filename: str, issue_type, issue_data: IssueResults):
    analyzer = DjangoModelAnalyzer()
    analyzer.visit(create_file_tree(filename))
    issues = tuple(
        filter(lambda x: isinstance(x, issue_type), analyzer.issues)
    )
    assert issues
    assert len(issues) == 1
    found_issue = issues[0]

    assert found_issue.col == issue_data.col
    assert found_issue.lineno == issue_data.lineno
    assert found_issue.extra_data['model_name'] == issue_data.model_name
