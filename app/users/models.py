from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager

# Create your models here.


class CustomUser(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('username not found')

        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)

        if extra_fields.get("is_staff") is not True:
            raise ValueError('Superuser has to have is_staff being True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser has to have superuser being True')

        return self.create_user(username=username, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True, null=True, help_text='Enter your name')
    email = models.EmailField(null=True, unique=True, help_text='Enter your nickname')
    password = models.CharField(unique=True, help_text='Enter your password')
    objects = CustomUser()
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    def __str__(self):
        return self.username

