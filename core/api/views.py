from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from ..models import Certificate, Contact, Newsletter, Project, Skill
from .serializers import CertificateSerializer, ContactSerializer, NewsletterSerializer, ProjectSerializer, SkillSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # Allow any user to create a contact message, but restrict other actions to admin users
    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    # Avoid exposing unpublished projects to non-admin users
    def get_queryset(self):
        if self.request.user and self.request.user.is_staff:
            return Project.objects.all()
        return Project.objects.filter(published=True)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]  # ['create', 'update', 'partial_update', 'destroy']
        return super().get_permissions()
    
    # Avoid exposing unpublished skills to non-admin users
    def get_queryset(self):
        if self.request.user and self.request.user.is_staff:
            return Skill.objects.all()
        return Skill.objects.filter(published=True)
    

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]  # ['create', 'update', 'partial_update', 'destroy']
        return super().get_permissions()

    # Avoid exposing unpublished certificates to non-amdin users
    def get_queryset(self):
        if self.request.user and self.request.user.is_staff:
            return Certificate.objects.all()
        return Certificate.objects.filter(published=True)    
    
    

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]  # ['list', 'retrieve', 'update', 'partial_update', 'destroy']
        return super().get_permissions()
