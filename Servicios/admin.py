from django.contrib import admin
from .models import Servicio

# Register your models here.
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('titulo', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('titulo', 'contenido')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo', 'contenido', 'imagen')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
