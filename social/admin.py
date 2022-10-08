""" Registrando el módelo en el administrador"""

#Django
from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('key', 'name', 'url',)
    list_display_links = ('key', 'name')

    fieldsets = (
        ('Red social', {
            'fields' : (('name','key',))
        }),
        ('Enlace', {
            'fields': ('url',)
        }),

        ('Metadata', {
            'fields': (('created', 'updated'),)
        }),
    )

    readonly_fields = ('created', 'updated')
