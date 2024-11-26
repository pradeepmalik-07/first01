from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def jawan(request):
    return HttpResponse('<h1><marquee direction="right">King Khan Shaharukh</marquee></h1>')