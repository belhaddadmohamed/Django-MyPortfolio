from rest_framework import viewsets
from ..models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAdminUser

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAdminUser]