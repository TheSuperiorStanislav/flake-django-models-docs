class Model(object):
    pass


class BaseModel(Model):
    pass


class AbstractBaseUser(Model):
    121


class PermissionsMixin(Model):
    pass


class CharField(object):
    pass


class ForeignKey(object):
    pass


class AppUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    """Custom user model.

    Attributes:
        first_name (str): first name
        hey_name (int):
            heey

    """

    some_key = ForeignKey()
    first_name = CharField()
    last_name = CharField()
    hey_name = CharField()

    @property
    def test_property(self):
        return ''

    @property
    def test_property_test(self):
        """Hey"""
        return ''
