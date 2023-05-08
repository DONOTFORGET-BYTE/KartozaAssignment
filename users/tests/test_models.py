from django.test import TestCase

from users.models import Profile, UserActivity
from django.db.models.functions import Now
from django.contrib.auth.models import User

class ProfileModelTestCase(TestCase):
    def test_crud_on_profile(self):
        """This will create a user and confirm a profile was attached to the user
        It will perform basic crud operations on the profile model ,get ,update delete"""
        user = User.objects.create(username='shatt',password="1")
        assert Profile.objects.filter(user=user.id).exists()
        Profile.objects.filter(user=user.id).update(home_address='London Bridge')
        profile_from_db = Profile.objects.get(user=user.id)
        assert profile_from_db.home_address == 'London Bridge'
        assert Profile.objects.filter(user=user.id).delete()
    

class UserActivityModelTestCase(TestCase):
    def test_crud_on_user_activity(self):
        user = User.objects.create(username='shatt',password="1")
        user_activity = UserActivity.objects.create(user=user)
        assert UserActivity.objects.filter(id=user_activity.id).exists()
        assert UserActivity.objects.filter(id=user_activity.id).delete()