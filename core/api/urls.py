from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'project', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]