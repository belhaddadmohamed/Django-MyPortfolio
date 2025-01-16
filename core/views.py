from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .models import Project, Contact, UserVisit
from .forms import ContactForm
from django.utils import timezone


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    # Track user visits
    ip = get_client_ip(request)
    visit, created = UserVisit.objects.get_or_create(ip_address=ip)
    visit.visit_count += 1
    visit.last_visit = timezone.now()
    visit.save()

    projects = Project.objects.all()
    
    return render(request, 'core/index.html', {'projects':projects})



def contact_ajax_form(request):
    contact = Contact.objects.create(
        full_name = request.POST['full_name'],
        email = request.POST['email'],
        phone = request.POST['phone'],
        message = request.POST['message'],
    )
    contact.save()

    return JsonResponse({'bool':True})



def single_project(request):
    id = request.GET['id']
    project = Project.objects.get(id=id)
    project_details = render_to_string('core/async/project_details.html', {'project':project})

    return JsonResponse({'project_details': project_details})
