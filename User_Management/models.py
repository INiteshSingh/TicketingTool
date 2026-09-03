from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):

    def _create_user(self, Employee_ID, password, **extra_fields):

        if not Employee_ID:
            raise ValueError("Employee ID is necessary")

        user = self.model(
            Employee_ID=Employee_ID,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, Employee_ID=None, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(
            Employee_ID,
            password,
            **extra_fields
        )

    def create_superuser(self, Employee_ID=None, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self._create_user(
            Employee_ID,
            password,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):

    Employee_ID = models.CharField(
        unique=True,
        blank=False,
        max_length=8
    )

    name = models.CharField(
        max_length=225,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    date_joined = models.DateTimeField(
        default=timezone.now
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "Employee_ID"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
