""" Creando el modelo de paginas Secundarias"""

from django.db import models

class Page(models.Model):
    
    title = models.CharField(verbose_name ='Titulo', max_length = 200)
    content = models.TextField(verbose_name ='Contenido')
    order = models.SmallIntegerField(verbose_name ='Orden', default=0)
    created = models.DateTimeField(auto_now_add = True, verbose_name = ' Fecha de creación')
    updated = models.DateTimeField(auto_now =True, verbose_name = 'Fecha de edición')

    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
        ordering = ['order','title']

    def __str_(self):
        return self.title