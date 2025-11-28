from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})

def edit_project(request, project_id):
    project = get_object_or_404(Project, ProjectID=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/edit_project.html', {'form': form})

def delete_project(request, project_id):
    project = get_object_or_404(Project, ProjectID=project_id)
    if request.method == "POST":
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/delete_project.html', {'project': project})