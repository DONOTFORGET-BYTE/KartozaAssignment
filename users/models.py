from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.TextField(null=True,blank=True)
    phone_number = PhoneNumberField(null=True, unique=True)
    longitude = models.FloatField(null=True,default=0)
    latitude = models.FloatField(null=True,default=0)

    def __str__(self):
        return self.user.username
    


class UserActivity(models.Model):
    """This is a simple model that will keep track of the user login and logout activities"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    session_key = models.CharField(max_length=40, db_index=True,null=True)
    login = models.DateTimeField(null=True, default=None)
    logout = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.user.username
