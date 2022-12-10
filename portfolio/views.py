from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from portfolio.models import *
from portfolio.forms import UserRegisterForm, NewProjectForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    projects = Project.objects.all()
    context = {'projects' : projects, 'count_projects': projects.count()}
    return render(request, 'index.html', context)

@login_required
def new_project(request):
    current_user = get_object_or_404(User, pk = request.user.pk)
    if str(current_user) == "William":
        if request.method == "POST":
            form = NewProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = current_user
                project.save()
                
                messages.success(request, 'Proyecto registrado')
                return redirect('index')
        
        else:
            form = NewProjectForm()
    
        context = {'form': form}
        return render(request, "new_project.html", context)
    else:
        return redirect('index')

def project_details(request, title = None):
    project = Project.objects.get(title = title)
    images_project = ImageProject.objects.filter(project = project.id)
    context = {'project': project, 'images_project': images_project}
    return render(request, 'project_detail.html', context)

@login_required
def add_images_project(request, title = None):
    current_user = get_object_or_404(User, pk = request.user.pk)
    if str(current_user) == "William":
        if request.method == "POST":
            images = request.FILES.getlist('images')
            project = Project.objects.get(title = title)
            for image in images:
                project_images = ImageProject.objects.create(project = project, images = image)
                   
            messages.success(request, 'Imágenes agregadas')
            return HttpResponseRedirect(reverse('project-details', args=[str(title)]))
        
        else:
            form = NewProjectForm()
    
        context = {'form': form}
        return render(request, "add_images_project.html", context)
    else:
        return redirect('index')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')

    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, "registration/register.html", context)