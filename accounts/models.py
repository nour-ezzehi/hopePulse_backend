from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    ROLE_CHOICES = (
        ('campaign_creator', 'Campaign Creator'),
        ('donor', 'Donor'),
    )

    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=28, default="")
    biography = models.TextField(blank=True, null=True)
    role = models.CharField(choices=ROLE_CHOICES, default='donor', blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    profile_complete = models.BooleanField(default=False)
    phone_number_validator = RegexValidator(regex=r'^\d{8}$', message='Phone number must be exactly 8 digits.')
    telephone_number = models.CharField(validators=[phone_number_validator], blank=True, null=True)
    cin_validator = RegexValidator(regex=r'^\d{8}$', message='cin number must be exactly 8 digits')
    cin = models.CharField(validators=[cin_validator], max_length=8, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_role(self):
        """
        Checks if the user has the specified role.
        """
        return self.role

    def get_full_name(self):
        """
        Returns the full name of the user.
        """
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.email

    def is_profile_complete(self):
        """
        Check if the user's profile is complete.
        """
        return all([self.biography, self.first_name, self.last_name, self.cin, self.telephone_number])
