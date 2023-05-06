from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.TextField(null=True,blank=True)
    phone_number = PhoneNumberField(null=True, unique=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=3,null=True,blank=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=3,null=True,blank=True)

    def __str__(self):
        return self.user.username
