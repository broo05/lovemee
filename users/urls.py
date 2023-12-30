# appname/urls.py
from django.urls import path
from .views import love_calculator, index


urlpatterns = [
    path('calculate_love/', love_calculator, name='love_calculator'),
    path('',index, name='index')
]
