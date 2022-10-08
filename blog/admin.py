""" Register blog models in admin"""
from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    ordering = ('published',)
    readonly_fields = ('created', 'updated')
    list_display =('title', 'post_categories', 'author', 'published', 'image')
    list_display_links = ('title',)
    list_filter = ('author__username', 'categories__name',)
    search_fields = ('title', 'author__username', 'content')
    fieldsets = (
        ('Posts', {
            'fields': (('title','author'),('categories'),)
        }),

        ('Content', {
            'fields': ('image', 'content', 'published')
        }),

        ('Metadata', {
            'fields': (('created', 'updated'),)
        }),
    )

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorias'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display =('pk','name')
    list_display_links = ('pk', 'name')
    fieldsets = (
        ('Category', {
            'fields': ('name',)
        }),

        ('Metadata', {
            'fields': (('created', 'updated'),)
        }),
    )

    