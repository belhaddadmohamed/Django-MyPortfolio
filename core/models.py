from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='project', null=True)
    github_link = models.URLField(null=True, blank=True)
    website_link = models.URLField(null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    read_time = models.PositiveIntegerField(null=True, blank=True, help_text="Estimated read time in minutes")
    created_at = models.DateField(default=timezone.now)
    order = models.PositiveIntegerField(default=0, help_text="Order of appearance")
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='certificate', default='certificate/certified.png', null=True)
    certificate_link = models.URLField(null=True, blank=True)
    issuer = models.CharField(max_length=200, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Order of appearance")
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='skill', null=True, blank=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    # full_name = models.CharField(max_length=200, null=True)
    # phone = models.CharField(max_length=200, null=True)
    # subject = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email



class UserVisit(models.Model):
    visit_count = models.PositiveIntegerField(default=0)
    last_visit = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.visit_count} Visits // Last one on {self.last_visit.strftime('%Y-%m-%d %H:%M:%S')} from {self.ip_address}"