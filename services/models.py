""" Creación del modelo de servivios """
from django.db import models

class Services(models.Model):
    """ Services model """
    title = models.CharField(max_length = 200, verbose_name = 'Titulo')
    subtitle = models.CharField(max_length = 200, verbose_name = 'Subitulo')
    content = models.TextField(verbose_name = 'Contenido')
    image = models.ImageField(verbose_name = 'Imagenes', upload_to = 'services')
    created = models.DateTimeField(auto_now_add = True, verbose_name = ' Fecha de creación')
    updated = models.DateTimeField(auto_now =True, verbose_name = 'Fecha de edición')

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str_(self):
        return self.title
