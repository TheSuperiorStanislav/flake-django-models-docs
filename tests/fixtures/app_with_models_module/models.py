class PrimaryKey:
    pass


class CharField:
    pass


class ModelWithDMD1:
    id = PrimaryKey()


class ModelWithDMD2:
    """Model docstring.

    id (int): Id is id

    """

    id = PrimaryKey()
    first_name = CharField()


class ModelWithDMD3:
    """Model docstring.

    id (int): Id is id
    first_name (str): first_name is first_name

    """

    id = PrimaryKey()
    first_name = CharField()

    @property
    def last_name(self):
        return 'last_name'
