from django.contrib import admin
from .models import PerformanceReview, PerformanceReviewGoals

class PerformanceReviewGoalsInline(admin.TabularInline):
    model = PerformanceReviewGoals
    extra = 1
    fields = ('PerformanceGoals',)
    show_change_link = True

@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ('PerformanceReviewID', 'get_employee', 'get_manager', 'ReviewDate', 'Rating')
    list_select_related = ('EmpID', 'ManagerID')
    search_fields = (
        'EmpID__FirstName', 'EmpID__LastName',
        'ManagerID__FirstName', 'ManagerID__LastName',
        'Comments'
    )
    list_filter = ('ReviewDate',)
    inlines = (PerformanceReviewGoalsInline,)
    ordering = ('-ReviewDate',)
    fieldsets = (
        (None, {
            'fields': ('EmpID', 'ManagerID', 'ReviewDate', 'Rating', 'Comments')
        }),
    )

    def get_employee(self, obj):
        return f"{obj.EmpID.FirstName} {obj.EmpID.LastName}"
    get_employee.short_description = 'Employee'
    get_employee.admin_order_field = 'EmpID__LastName'

    def get_manager(self, obj):
        if obj.ManagerID:
            return f"{obj.ManagerID.FirstName} {obj.ManagerID.LastName}"
        return "-"
    get_manager.short_description = 'Manager'
    get_manager.admin_order_field = 'ManagerID__LastName'


@admin.register(PerformanceReviewGoals)
class PerformanceReviewGoalsAdmin(admin.ModelAdmin):
    list_display = ('PerformanceReviewID', 'get_review', 'short_goal')
    search_fields = ('PerformanceGoals',)
    list_select_related = ('PerformanceReviewID',)

    def get_review(self, obj):
        return f"{obj.PerformanceReviewID.PerformanceID}"
    get_review.short_description = 'Review ID'

    def short_goal(self, obj):
        text = obj.PerformanceGoals or ''
        return (text[:75] + '...') if len(text) > 75 else text
    short_goal.short_description = 'Goal'