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


class AppUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    """Custom user model.

    Attributes:
        first_name (str): first name

    """

    first_name = CharField()
    last_name = CharField()

    choices = [
        'pasta',
        'pizza',
    ]
