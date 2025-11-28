from django.shortcuts import render, get_object_or_404, redirect
from .models import PerformanceReview, PerformanceReviewGoals
from employees.models import Employee

def performance_review_list(request):
    reviews = PerformanceReview.objects.select_related('EmpID', 'ManagerID')
    return render(request, 'performance_review/performance_review_list.html', {'reviews': reviews})


def add_performance_review(request):
    employees = Employee.objects.all()

    if request.method == "POST":
        emp = Employee.objects.get(EmpID=request.POST['EmpID'])
        manager = Employee.objects.get(EmpID=request.POST['ManagerID'])
        review_date = request.POST.get("ReviewDate")
        rating = request.POST.get("Rating")
        comments = request.POST.get("Comments")

        review = PerformanceReview.objects.create(
            EmpID=emp,
            ManagerID=manager,
            ReviewDate=review_date,
            Rating=rating,
            Comments=comments,
        )

        goals = request.POST.getlist("goals[]")
        for g in goals:
            if g.strip():
                PerformanceReviewGoals.objects.create(
                    PerformanceReviewID=review,
                    PerformanceGoals=g
                )

        return redirect('performance_review_list')

    return render(request, 'performance_review/add_performance_review.html', {'employees': employees})


def edit_performance_review(request, pk):
    review = get_object_or_404(PerformanceReview, pk=pk)
    employees = Employee.objects.all()

    if request.method == "POST":
        review.EmpID = Employee.objects.get(EmpID=request.POST['EmpID'])
        review.ManagerID = Employee.objects.get(EmpID=request.POST['ManagerID'])
        review_date = request.POST.get('ReviewDate')
        if review_date:
            review.ReviewDate = review_date
        review.Rating = request.POST['Rating']
        review.Comments = request.POST['Comments']
        review.save()
        return redirect('performance_review_list')

    return render(request, 'performance_review/edit_performance_review.html', {'review': review, 'employees': employees})


def edit_performance_review_goals(request, pk):
    review = get_object_or_404(PerformanceReview, pk=pk)
    goals = PerformanceReviewGoals.objects.filter(PerformanceReviewID=review)

    if request.method == "POST":
        for goal in goals:
            field_name = f"goal_{goal.pk}"
            new_text = request.POST.get(field_name)
            if new_text is not None:
                goal.PerformanceGoals = new_text
                goal.save()

        return redirect('performance_review_list')

    return render(request, 'performance_review/performance_goals_list.html', {'review': review,'goals': goals})


def delete_performance_review(request, pk):
    review = get_object_or_404(PerformanceReview, pk=pk)

    if request.method == "POST":
        review.delete()
        return redirect('performance_review_list')

    return render(request, 'performance_review/delete_performance_review.html', {'review': review})