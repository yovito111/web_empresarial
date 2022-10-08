""" Pages urls"""
#Django
from django.urls import path
from . import views

urlpatterns = [
    #blog paths
    path('<int:page_id>/<slug:page_slug>', views.page, name="page"),
]