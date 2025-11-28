from django.shortcuts import render, redirect, get_object_or_404
from .models import EmployeeTraining
from .forms import EmployeeTrainingForm

def emp_training_list(request):
    emp_trainings = EmployeeTraining.objects.all()
    return render(request, 'emp_training/emp_training_list.html', {'emp_trainings': emp_trainings})

def add_emp_training(request):
    if request.method == "POST":
        form = EmployeeTrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_training_list')
    else:
        form = EmployeeTrainingForm()
    return render(request, 'emp_training/add_emp_training.html', {'form': form})

def edit_emp_training(request, emp_training_id):
    emp_training = get_object_or_404(EmployeeTraining, pk=emp_training_id)
    if request.method == "POST":
        form = EmployeeTrainingForm(request.POST, instance=emp_training)
        if form.is_valid():
            form.save()
            return redirect('emp_training_list')
    else:
        form = EmployeeTrainingForm(instance=emp_training)
    return render(request, 'emp_training/edit_emp_training.html', {'form': form})

def delete_emp_training(request, emp_training_id):
    emp_training = get_object_or_404(EmployeeTraining, pk=emp_training_id)
    if request.method == "POST":
        emp_training.delete()
        return redirect('emp_training_list')
    return render(request, 'emp_training/delete_emp_training.html', {'emp_training': emp_training})