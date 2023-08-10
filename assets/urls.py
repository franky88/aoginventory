from django.urls import path
from assets.views.department import department_view, department_view_details, department_view_delete
from assets.views.employee import employee_view, employee_view_details, employee_view_active_status_update

app_name = "assets"
urlpatterns = [
    path("", employee_view, name="employee_view"),
    path("details/<employee_id>", employee_view_details, name="employee_view_details"),
    path("details/status/<employee_id>", employee_view_active_status_update, name="employee_view_active_status_update"),
    path("departments", department_view, name="department_list"),
    path("departments/update/<pk>", department_view_details, name="department_view_details"),
    path("departments/delete/<pk>", department_view_delete, name="department_view_delete"),
]