from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from ..models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()