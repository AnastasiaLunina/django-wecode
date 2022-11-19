from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {
        'project': projectObj,
    }
    return render(request, 'projects/single-project.html', context)

@login_required(login_url = 'login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        # request.FILES needed to submit images uploaded by user
        form = ProjectForm(request.POST, request.FILES) 
        if form.is_valid():
            # This giving the instance of a project and we can update data in current project
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {
        'form': form,
    }
    return render(request, 'projects/project_form.html', context)


@login_required(login_url = 'login')
def updateProject(request, pk):
    # getting data for only one profile to make sure only account owner can update
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form': form,
    }
    return render(request, 'projects/project_form.html', context)

@login_required(login_url = 'login')
def deleteProject(request, pk):
    # getting data for only one profile to make sure only account owner can update
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
        
    context = {
        'object': project,
    }
    return render(request, 'delete_template.html', context)