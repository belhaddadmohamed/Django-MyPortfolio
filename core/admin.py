from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Project, Contact, UserVisit

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['email', 'message', 'created_at']
    readonly_fields = ['created_at']

class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'github_link', 'website_link']

class UserVisitAdmin(admin.ModelAdmin):
    list_display = [ 'ip_address', 'last_visit','visit_count']
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(UserVisit, UserVisitAdmin)