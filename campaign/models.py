from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
from django.conf import settings

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class City(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    phone_number_validator = RegexValidator(regex=r'^\d{8}$', message='Phone number must be exactly 8 digits.')
    telephone_number = models.PositiveIntegerField(validators=[phone_number_validator])
    beneficiary = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    story = models.TextField()
    num_of_donation = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name
