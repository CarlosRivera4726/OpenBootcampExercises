from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.


def index(request):
    return HttpResponse("Todo Ok!")


def create(request):
    # Creamos los elementos
    place = Place(name="Lugar 1", address="Calle 4A #52 D-10")
    place.save()

    restaurant = Restaurant(place=place, number_of_employees=5)
    restaurant.save()
    return HttpResponse(restaurant)
    