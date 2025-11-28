from django.contrib.auth import authenticate, login, logout
from django.urls import path, include
from django.shortcuts import render, redirect
from django.contrib import admin, messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("/dashboard/")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html", {"error": "Invalid username or password."})

    return render(request, "login.html")

@login_required
def dashboard_view(request):
    return render(request, "dashboard.html", {"user": request.user})

def logout_view(request):
    logout(request)
    return render(request, "logout.html")

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('admin/', admin.site.urls),

    path('', include('employees.urls')),
    path('departments/', include('departments.urls')),
    path('employees/', include('employees.urls')),
    path('projects/', include('projects.urls')),
    path('attendance/', include('attendance.urls')),
    path('training/', include('training.urls')),
    path('emp_projects/', include('emp_projects.urls')),
    path('emp_training/', include('emp_training.urls')),
    path('payroll/', include('payroll.urls')),
    path('leave_request/', include('leave_request.urls')),
    path('performance_review/', include('performance_review.urls')),

    path('api/employees/', include('employees.api_urls')),
    path('api/departments/', include('departments.api_urls')),
    path('api/projects/', include('projects.api_urls')),
    path('api/attendance/', include('attendance.api_urls')),
    path('api/training/', include('training.api_urls')),
    path('api/emp_projects/', include('emp_projects.api_urls')),
    path('api/emp_training/', include('emp_training.api_urls')),
    path('api/payroll/', include('payroll.api_urls')),
    path('api/leave_request/', include('leave_request.api_urls')),
    path('api/performance_review/', include('performance_review.api_urls')),
]