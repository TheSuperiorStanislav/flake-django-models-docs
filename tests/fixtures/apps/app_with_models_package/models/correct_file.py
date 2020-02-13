class PrimaryKey:
    pass


class ForeignKey:
    pass


class CharField:
    pass


class CorrectModel:
    """Model docstring.

    id (int): Id is id
    user (User): User is user
    first_name (list[str]): first_name is first_name

    """

    id = PrimaryKey()
    user = ForeignKey()
    first_name = CharField()

    @property
    def last_name(self):
        """Property docstring."""
        return 'last_name'

    @staticmethod()
    def trans(self):
        return 'last_name'
