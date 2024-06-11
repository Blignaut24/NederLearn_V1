# Standard library imports
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Landing page view
def display_landing_page(request):
    return HttpResponse("Welcome to the Nederlearn App!")
