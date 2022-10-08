"""Services views mode"""
from django.shortcuts import render
from .models import Services

# Create your views here.
def services(request):
    """ Services view"""
    services = Services.objects.all()
    return render(request, 'services/services.html', {'services': services})
