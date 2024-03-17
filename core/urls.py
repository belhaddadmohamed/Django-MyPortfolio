from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('single-project/', views.single_project, name='single_project'),
    path('contact-ajax-form/', views.contact_ajax_form, name='contact_ajax_form'),
]