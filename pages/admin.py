""" Registrando el modelo pages en el admin"""
from django.contrib import admin
from .models import Page

@admin.register(Page)
class PAgeAdmin(admin.ModelAdmin):
    list_display = ('title','order')
    list_display_links = ('title',)

    fieldsets = (
        ('Paginas', {
            'fields' : (('title','order'))
        }),
        ('Contenido', {
            'fields': ('content',)
        }),

        ('Metadata', {
            'fields': (('created', 'updated'),)
        }),
    )

    readonly_fields = ('created', 'updated')
 