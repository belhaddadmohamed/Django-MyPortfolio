from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from ..models import Certificate, Contact, Newsletter, Project, Skill
from .serializers import CertificateSerializer, ContactSerializer, NewsletterSerializer, ProjectSerializer, SkillSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

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
            self.permission_classes = [IsAdminUser]  # ['create', 'update', 'partial_update', 'destroy']
        return super().get_permissions()


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]  # ['create', 'update', 'partial_update', 'destroy']
        return super().get_permissions()
    

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]  # ['create', 'update', 'partial_update', 'destroy']
        return super().get_permissions()
    

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]  # ['list', 'retrieve', 'update', 'partial_update', 'destroy']
        return super().get_permissions()
