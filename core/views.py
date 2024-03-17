from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .models import Project, Contact
from .forms import ContactForm


def index(request):
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
