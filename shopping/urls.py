from shopping.views import *
from django.urls import path

app_name='shopping'

urlpatterns=[
    path('mens/',mens,name='mens'),
]