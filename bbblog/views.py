from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home_page(request):
    return HttpResponse("this is home page")

def hello(request):
    return HttpResponse("hell oworld")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "it is now " +  now
    return HttpResponse(now)