# Mixins
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Settings and utils
from django.db import models
from django.utils import timezone


class UserAccountManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("Users must haven a name")

        username = self.model.normalize_username(username)

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField("date joined", default=timezone.now)
    date_expired = models.DateTimeField("date expired", default=timezone.now)

    objects = UserAccountManager()
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
