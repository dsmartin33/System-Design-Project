from django.contrib.auth import authenticate, login
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

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),
    path('', include('employees.urls')),
    path('api/departments/', include('departments.urls')),
]