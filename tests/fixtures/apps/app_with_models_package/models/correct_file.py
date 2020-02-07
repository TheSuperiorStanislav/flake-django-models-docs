class PrimaryKey:
    pass


class CharField:
    pass


class CorrectModel:
    """Model docstring.

    id (int): Id is id
    first_name (str): first_name is first_name

    """

    id = PrimaryKey()
    first_name = CharField()

    @property
    def last_name(self):
        """Property docstring."""
        return 'last_name'
