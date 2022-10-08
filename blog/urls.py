""" Blog urls"""
#Django
from django.urls import path
from . import views

urlpatterns = [
    #blog paths
    path('category/<int:category_id>/', views.category, name="category"),
    path('', views.blog, name='blog'),
]