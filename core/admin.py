from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Newsletter, Project, Contact, UserVisit, Skill, Certificate

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['email', 'message', 'created_at']
    readonly_fields = ['created_at']

class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'github_link', 'website_link', 'published', 'order']
    list_editable = ['published', 'order']

class UserVisitAdmin(admin.ModelAdmin):
    list_display = [ 'ip_address', 'last_visit','visit_count']

class SkillAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'published']
    list_editable = ['published']

class CertificateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'issuer', 'image', 'issue_date', 'published', 'order']
    list_editable = ['published', 'order', 'image']  

class NewsletterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']
    list_editable = ['is_active']
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(UserVisit, UserVisitAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Newsletter, NewsletterAdmin)