# Employee Management System - Django + MySQL (EMS Backend)

This is a professional Django project scaffold for an Employee Management System using **MySQL**.
It includes models for: Attendance, Department, EmployeeProject, Employees, EmployeeTraining, LeaveRequest, Payroll, PerformanceReview, Project, and Training.

## Quickstart (development)

1. Create a Python virtualenv (Python 3.12 recommended)
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file (see `.env.example`) and set your MySQL credentials.
4. Run migrations, seed data, and start the server:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py seed_data
   python manage.py runserver
   ```

API root: `http://127.0.0.1:8000/api/`

Notes:
* Authentication is disabled (AllowAny) per user request.
* For production: set `DEBUG=False`, configure `ALLOWED_HOSTS`, and use proper secret management.
