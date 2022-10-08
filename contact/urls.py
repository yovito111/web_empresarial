"""Contact urls"""
#Django
from django.urls import path
from . import views

urlpatterns = [
    #Contact paths
    path('', views.contact, name='contact'),
]