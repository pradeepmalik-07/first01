from django.urls import path
from BOLLYWOOD.views import *

urlpatterns=[
    path('jawan/',jawan,name='jawan')
]