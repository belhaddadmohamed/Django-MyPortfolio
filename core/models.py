from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='project', null=True)
    github_link = models.URLField(null=True, blank=True)
    website_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
    


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200, null=True)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    


class UserVisit(models.Model):
    visit_count = models.PositiveIntegerField(default=0)
    last_visit = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.visit_count} Visits on {self.last_visit.strftime('%Y-%m-%d %H:%M:%S')} from {self.ip_address}"