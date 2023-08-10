from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant


def create(request):
    #crear elemento 
    place = Place(name='lugar1', address='call demo')
    place.save()

    restaurant = Restaurant(place=place, number_of_employees=8)
    restaurant.save()
    return HttpResponse(restaurant.place.name)
