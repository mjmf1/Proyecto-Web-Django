from django.contrib import admin
from .models import Post, Categoria

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('nombre', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('nombre',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('nombre',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Categoria, CategoriaAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('titulo', 'autor', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'autor')
    search_fields = ('titulo', 'contenido')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo', 'contenido', 'imagen', 'autor', 'categoria')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Post, PostAdmin)