from django.contrib import admin
from .models import Project, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'message']

admin.site.register(Project)
admin.site.register(Contact, ContactAdmin)