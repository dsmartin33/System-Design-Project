from django.core.management.base import BaseCommand
from employees.models import *
from datetime import date

class Command(BaseCommand):
    help = 'Seed minimal example data for EMS'

    def handle(self, *args, **kwargs):
        # Clear some tables (use carefully)
        EmployeeProject.objects.all().delete()
        EmployeeTraining.objects.all().delete()
        Attendance.objects.all().delete()
        LeaveRequest.objects.all().delete()
        Payroll.objects.all().delete()
        PerformanceReview.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()
        Project.objects.all().delete()
        Training.objects.all().delete()

        d1 = Department.objects.create(name='Human Resources', location='HQ')
        d2 = Department.objects.create(name='Engineering', location='R&D')

        p1 = Project.objects.create(name='Website Revamp', description='Frontend & Backend update', start_date=date(2024,1,10))
        p2 = Project.objects.create(name='Mobile App', description='iOS & Android', start_date=date(2024,5,1))

        t1 = Training.objects.create(title='Security Awareness', date=date(2024,2,20))
        t2 = Training.objects.create(title='Django Advanced', date=date(2024,3,15))

        e1 = Employee.objects.create(first_name='Alice', last_name='Johnson', email='alice@example.com', department=d2, hire_date=date(2023,7,1))
        e2 = Employee.objects.create(first_name='Bob', last_name='Smith', email='bob@example.com', department=d1, hire_date=date(2022,4,20))

        EmployeeProject.objects.create(employee=e1, project=p1, role='Backend Developer', assigned_date=date(2024,1,15))
        EmployeeTraining.objects.create(employee=e1, training=t2, completed=True)

        Attendance.objects.create(employee=e1, date=date(2024,9,1), status='present')
        LeaveRequest.objects.create(employee=e2, start_date=date(2024,9,10), end_date=date(2024,9,12), reason='Personal')
        Payroll.objects.create(employee=e1, period_start=date(2024,8,1), period_end=date(2024,8,31), gross_amount=7500, net_amount=6000, tax=1500)
        PerformanceReview.objects.create(employee=e1, reviewer_name='CTO', review_date=date(2024,8,15), rating=4, comments='Strong performance')

        self.stdout.write(self.style.SUCCESS('Seeded example EMS data'))
