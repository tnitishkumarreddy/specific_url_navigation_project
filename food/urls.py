from food.views import *
from django.urls import path
app_name='food'

urlpatterns=[
    path('nonveg/',nonveg,name='nonveg'),
]