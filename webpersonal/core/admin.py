from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_created_at')
    list_filter = ('create_at',)
    list_editable = ('title',)
    list_display_links = ('get_created_at',)

    def get_created_at(self, obj):
        return obj.create_at
    get_created_at.short_description = 'Fecha de Creación'

admin.site.register(Project, ProjectAdmin)
