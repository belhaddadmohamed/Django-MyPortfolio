from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, ProjectViewSet, SkillViewSet

router = DefaultRouter()
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'project', ProjectViewSet, basename='project')
router.register(r'skill', SkillViewSet, basename='skill')

urlpatterns = [
    path('', include(router.urls)),
]