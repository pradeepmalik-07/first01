from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Toxic(request):
    return HttpResponse('<h1><marquee direction="right">This content can be read, appended to, or replaced</marquee></h1>')