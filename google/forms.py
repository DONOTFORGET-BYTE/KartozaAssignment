from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

mode_of_transport = [
  ("Driving","driving"),
  ("Bicycling","bicycling"),
  ("Walking","walking"),
  ("Transit","transit"),
]

