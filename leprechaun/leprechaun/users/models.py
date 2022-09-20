from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from leprechaun.core.models import BaseModel
from leprechaun.users.configs import GENDER_CHOICES
# from leprechaun.users.managers import UserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.first_name = kwargs.get("first_name", "")
        user.last_name = kwargs.get("last_name", "")
        user.phone_number = kwargs.get("phone_number", "")
        user.date_of_birth = kwargs.get("date_of_birth")
        user.is_active = False

        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """

        user = self.create_user(email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField("Email", unique=True, max_length=256)
    is_active = models.BooleanField("Is Active", default=True)
    is_deleted = models.BooleanField("Is Deleted", default=False)
    is_superuser = models.BooleanField("Is Superuser", default=False, db_index=True)
    is_staff = models.BooleanField("Is Staff", default=False, db_index=True)

    # metadata
    first_name = models.CharField("First Name", max_length=64, default="", blank=True)
    last_name = models.CharField("Last Name", max_length=64, default="", blank=True)
    address = models.CharField("Address", max_length=128, null=True, blank=True)
    phone_number = models.CharField("Phone Number", max_length=20, default="", blank=True)
    date_of_birth = models.DateField("Date Of Birth", null=True, blank=True)
    postcode = models.CharField("Postcode", max_length=32, blank=True)
    gender = models.CharField("Gender", max_length=11, choices=GENDER_CHOICES, default="", blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    class Meta:
        app_label = "users"
        verbose_name_plural = "Users"
        ordering = ["-modified"]

    def __str__(self) -> str:
        return f"{self.get_full_name()} (user {self.id})"

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None) -> bool:
        return self.is_superuser

    def has_module_perms(self, app_label) -> bool:
        return self.is_superuser
