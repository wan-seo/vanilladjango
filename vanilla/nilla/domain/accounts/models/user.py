from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = "accounts_user"
