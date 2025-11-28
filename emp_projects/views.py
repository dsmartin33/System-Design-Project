from django.shortcuts import render, redirect, get_object_or_404
from .models import EmployeeProject
from .forms import EmployeeProjectForm

def emp_projects_list(request):
    emp_projects = EmployeeProject.objects.all()
    return render(request, 'emp_projects/emp_projects_list.html', {'emp_projects': emp_projects})

def add_emp_projects(request):
    if request.method == "POST":
        form = EmployeeProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_projects_list')
    else:
        form = EmployeeProjectForm()
    return render(request, 'emp_projects/add_emp_projects.html', {'form': form})

def edit_emp_projects(request, pk_id):
    emp_project = get_object_or_404(EmployeeProject, pk=pk_id)
    if request.method == "POST":
        form = EmployeeProjectForm(request.POST, instance=emp_project)
        if form.is_valid():
            form.save()
            return redirect('emp_projects_list')
    else:
        form = EmployeeProjectForm(instance=emp_project)
    return render(request, 'emp_projects/edit_emp_projects.html', {'form': form})

def delete_emp_projects(request, pk_id):
    emp_projects = get_object_or_404(EmployeeProject, pk=pk_id)
    if request.method == "POST":
        emp_projects.delete()
        return redirect('emp_projects_list')
    return render(request, 'emp_projects/delete_emp_projects.html', {'emp_projects': emp_projects})