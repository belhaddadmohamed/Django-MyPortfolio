from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from ..models import Contact, Project
from .serializers import ContactSerializer, ProjectSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_permissions(self):
        if self.action == 'create':
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
    