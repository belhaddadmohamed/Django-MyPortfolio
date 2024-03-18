from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Project, Contact

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['full_name', 'email', 'message']

class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'github_link']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)