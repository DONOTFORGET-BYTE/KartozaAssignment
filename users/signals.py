from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth import user_logged_in, user_logged_out
from django.db.models.functions import Now

from .models import Profile, UserActivity

"""Signals defined in this will do the following
1. when a user registers a profile is created for them
2. when updating user information via the profile page
3. when a user logs in the activity is recorded 
4. when a user logs out the activity is recorded"""

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



@receiver(user_logged_in)
def register_login(sender, user, request, **kwargs):
    UserActivity.objects.create(
        user=user,
        session_key=request.session.session_key
    )

@receiver(user_logged_out)
def register_logout(sender, user, request, **kwargs):
    UserActivity.objects.filter(
        user=user,
        session_key=request.session.session_key
    ).update(
        logout=Now()
    )
