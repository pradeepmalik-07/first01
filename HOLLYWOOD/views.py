from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Mission_Impossible(request):
    return HttpResponse('<h1>Tom Cruise</h1>')