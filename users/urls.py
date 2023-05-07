from django.urls import path
from .views import home, profile, RegisterView, evoke_modal

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('evoke/', evoke_modal, name='evoke_modal')
]
