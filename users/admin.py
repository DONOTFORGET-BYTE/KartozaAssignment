from django.contrib import admin
from .models import Profile
from .models import UserActivity

# Register models to the admin panel

admin.site.register(Profile)
admin.site.register(UserActivity)
