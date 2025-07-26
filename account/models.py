from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Defining Custom user model earlier,
    because it would make it easier to customize
    user model if needed in future.
    """

    pass
