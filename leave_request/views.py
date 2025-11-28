from django.shortcuts import render, redirect, get_object_or_404
from .models import LeaveRequest
from .forms import LeaveRequestForm

def leave_request_list(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'leave_request/leave_request_list.html', {'leave_requests': leave_requests})

def add_leave_request(request):
    if request.method == "POST":
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_request_list')
    else:
        form = LeaveRequestForm()
    return render(request, 'leave_request/add_leave_request.html', {'form': form})

def edit_leave_request(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    if request.method == "POST":
        form = LeaveRequestForm(request.POST, instance=leave_request)
        if form.is_valid():
            form.save()
            return redirect('leave_request_list')
    else:
        form = LeaveRequestForm(instance=leave_request)
    return render(request, 'leave_request/edit_leave_request.html', {'form': form})

def delete_leave_request(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    if request.method == "POST":
        leave_request.delete()
        return redirect('leave_request_list')
    return render(request, 'leave_request/delete_leave_request.html', {'leave_request': leave_request})