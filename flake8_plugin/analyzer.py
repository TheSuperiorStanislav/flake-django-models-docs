import re
import typing
from ast import AST, Assign, Call, ClassDef, Expr, FunctionDef, NodeVisitor

from .issue import DMD1, DMD2, DMD3, Issue


class DjangoModelAnalyzer(NodeVisitor):
    """Class which analyzes the code of django models files.

    Attributes:
        field_docstring_pattern (str): Regex for checking docstrings
        issues (list[Issue]): List of issues found in code

    """

    field_docstring_pattern = r'{field} \([a-z._]*\):( \S|\n\s*\S)'

    def __init__(self):
        """Initiate analyzer."""
        self.issues: typing.List[Issue] = []

    def visit_ClassDef(self, node: ClassDef):
        """Analyze all classes in file(tree)."""
        self.check_main_docs(node)
        self.check_properties_docs(node)

    def check_main_docs(self, node: ClassDef):
        """Check the main docs of model class."""
        fields = self.extract_fields_from_model(node)

        # If class doesn't have any fields we assume that is not a Model class
        if not fields:
            return

        if not self.check_docs_existence(node):
            self.issues.append(DMD1(
                lineno=node.lineno,
                col=node.col_offset,
                model_name=node.name,
            ))
            return

        fields = self.extract_fields_from_model(node)
        docs = self.extract_docstring_from_model(node)

        for field in fields:
            field_name = field.targets[0].id
            if not self.is_main_docs_is_ok(field_name=field_name, docs=docs):
                self.issues.append(DMD2(
                    lineno=field.lineno,
                    col=field.col_offset,
                    model_name=node.name,
                    field=field_name,
                ))

    def check_properties_docs(self, node: ClassDef):
        """Checks docs existences for properties."""
        properties = self.extract_properties_from_model(node)
        for property_def in properties:
            if not self.check_docs_existence(property_def):
                self.issues.append(
                    DMD3(
                        lineno=property_def.lineno,
                        col=node.col_offset,
                        model_name=node.name,
                        property=property_def.name
                    )
                )

    def extract_fields_from_model(self, node: ClassDef):
        """Extract from class body all fields."""
        fields = [
            body_part
            for body_part in node.body
            if self.is_model_field_assigment(body_part)
        ]
        return fields

    def extract_properties_from_model(self, node: ClassDef):
        """Extract `propertied` from model class."""
        properties = (
            body_part
            for body_part in node.body
            if self.is_property(body_part)
        )
        return properties

    def is_model_field_assigment(self, body_part: AST) -> bool:
        """Check is a part of model class body is field assigment.

        Examples:
            some_key = ForeignKey() => return True
            first_name = CharField() => return True
            choices = ['1', '2', '3'] => return False

        """
        is_field_assigment = (
                isinstance(body_part, Assign)
                and isinstance(body_part.value, Call)
        )
        if not is_field_assigment:
            return False
        return (
            'Field' in self.get_field_type(body_part) or
            'Key' in self.get_field_type(body_part)
        )

    def is_main_docs_is_ok(self, field_name: str, docs: str) -> bool:
        """Check if docstring of model class contains decs for all fields."""
        pattern = self.field_docstring_pattern.format(field=field_name)
        return bool(re.search(pattern=pattern, string=docs))

    @staticmethod
    def is_property(body_part: AST) -> bool:
        """Check if body part is `property` of model."""
        if not isinstance(body_part, FunctionDef):
            return False

        decorators = (
            decorator.id
            for decorator in body_part.decorator_list
        )
        return 'property' in decorators

    @staticmethod
    def get_field_type(body_part) -> str:
        """Get field type form class.

        Examples:
            CharField
            ForeignKey

        """
        field_type = getattr(body_part.value.func, 'attr', None)
        if not field_type:
            field_type = getattr(body_part.value.func, 'id', None)
        return field_type

    @staticmethod
    def extract_docstring_from_model(node: ClassDef) -> str:
        """Extract docstring form model class."""
        return node.body[0].value.value

    @staticmethod
    def check_docs_existence(
            node: typing.Union[ClassDef, FunctionDef]
    ) -> bool:
        """Check is class or function has a docstring."""
        return isinstance(node.body[0], Expr)
