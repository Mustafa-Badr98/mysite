from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from datetime import datetime


class UsersManger(BaseUserManager):
    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            user_name=user_name,
            **other_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, password, **other_fields):
        """
        Creates and saves a superuser with the given email and password.
        """

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("super user must be assigned is_staff = True")

        if other_fields.get('is_superuser') is not True:
            raise ValueError("super user must be assigned is_superuser = True")

        return self.create_user(email, user_name, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=True
    )
    user_name = models.CharField(max_length=150, blank=True, unique=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    mobile_phone = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='user_groups',
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='user_permissions',
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    REQUIRED_FIELDS = ['user_name', ]
    USERNAME_FIELD = 'email'

    objects = UsersManger()

    def __str__(self):
        return f'{self.email}'

    @classmethod
    def get_all_users(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_user(cls, email):
        return cls.objects.filter(email=email).first()
