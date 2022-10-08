from .models import Services
from django.contrib import admin

# Register your models here.
@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):

    
    list_display = ('pk', 'title', 'subtitle', 'image')
    list_display_links = ('pk', 'title')

    fieldsets = (
        ('Services', {
            'fields' : (('title','subtitle','image'))
        }),
        ('Descripción', {
            'fields': ('content',)
        }),

        ('Metadata', {
            'fields': (('created', 'updated'),)
        }),
    )

    readonly_fields = ('created', 'updated')