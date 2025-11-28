from django.shortcuts import render, redirect, get_object_or_404
from .models import Training
from .forms import TrainingForm

def training_list(request):
    trainings = Training.objects.all()
    return render(request, 'training/training_list.html', {'trainings': trainings})

def add_training(request):
    if request.method == "POST":
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingForm()
    return render(request, 'training/add_training.html', {'form': form})

def edit_training(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == "POST":
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingForm(instance=training)
    return render(request, 'training/edit_training.html', {'form': form})

def delete_training(request, pk):
    training = get_object_or_404(Training, pk=pk)
    if request.method == "POST":
        training.delete()
        return redirect('training_list')
    return render(request, 'training/delete_training.html', {'training': training})