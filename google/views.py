from asyncio.windows_events import NULL
import googlemaps
import gmaps
from datetime import datetime
from django.shortcuts import render, redirect, reverse
from .forms import *
from .models import *
from django.http import JsonResponse
from django.conf import settings
from users.models import Profile


def home(request):
    context = {}
    return render(request, 'users/templates/users/home.html',context)

# method renders the map
def map(request):
    key = settings.GOOGLE_API_KEY
    context = {
        'key':key,
    }
    return render(request, 'map.html',context)


def user_locations(request):
    """This function fetches all the users registered and returns the json object to the frontend"""
    result_list = list(Profile.objects\
                .exclude(latitude__isnull=True)\
                .exclude(longitude__isnull=True)\
                .exclude(latitude__exact=0)\
                .exclude(longitude__exact=0)\
                .values('id',
                        'home_address', 
                        'latitude',
                        'longitude'
                        ))
  
    return JsonResponse(result_list, safe=False)
