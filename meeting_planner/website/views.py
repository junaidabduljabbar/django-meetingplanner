from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")

def date(request):
    return HttpResponse("The current datetime is" + str(datetime.now()))