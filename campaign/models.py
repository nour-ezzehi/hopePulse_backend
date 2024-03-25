from django.db import models
from accounts.models import CustomUser
from django.core.validators import RegexValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

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
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    beneficiary = models.CharField(max_length=100)
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    story = models.TextField()
    num_of_donation = models.PositiveBigIntegerField(default=0)
    num_of_donators = models.PositiveBigIntegerField(default = 0)
    current_amount_raised = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Charity(models.Model):
  name = models.CharField(max_length=100)
  phone_number_validator = RegexValidator(regex=r'^\d{8}$', message='Phone number must be exactly 8 digits.')
  telephone_number = models.PositiveIntegerField(validators=[phone_number_validator])
  contact_email = models.EmailField(("email address"), unique=True)
  physical_address = models.CharField(max_length = 28)
  mission = models.TextField()
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  is_approved = models.BooleanField(default=False)

class Donation(models.Model):
    donor_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    recipient_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    recipient_id = models.PositiveIntegerField()
    recipient_object = GenericForeignKey('recipient_type', 'recipient_id')

class Comment(models.Model):
  campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  text = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
