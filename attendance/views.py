from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance
from .forms import AttendanceForm

def attendance_list(request):
    attendance_records = Attendance.objects.select_related('EmpID').all()
    return render(request, 'attendance/attendance_list.html', {'attendance_records': attendance_records})

def add_attendance(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/add_attendance.html', {'form': form})

def edit_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, EmpID=attendance_id)
    if request.method == "POST":
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'attendance/edit_attendance.html', {'form': form})

def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, EmpID=attendance_id)
    if request.method == "POST":
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'attendance/delete_attendance.html', {'attendance': attendance})