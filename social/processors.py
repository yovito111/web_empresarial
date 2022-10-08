from signal import CTRL_C_EVENT


""" Creando procesadores de  contexto"""
from .models import Link
def ctx_dic(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx