from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST
from assets.forms.employee import EmployeeForm
from assets.models.employee import Employee

def employee_view(request):
    form = EmployeeForm(request.POST or None)
    employees = Employee.objects.all()
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('assets:employee_view')
    context = {
        "title": "employee list",
        "form": form,
        "employees": employees
    }
    return render(request, 'employees/list.html', context)

def employee_view_details(request, employee_id):
    instance = get_object_or_404(Employee, employee_id=employee_id)
    form = EmployeeForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('assets:employee_view_details', employee_id=instance.employee_id)
    context = {
        "title": "employee details",
        "form": form,
        "instance": instance
    }
    return render(request, 'employees/details.html', context)

@require_POST
def employee_view_active_status_update(request, employee_id):
    instance = get_object_or_404(Employee, employee_id=employee_id)
    if request.method == "POST":
        if instance.is_active:
            instance.is_active = False
            instance.save()
        else:
            instance.is_active = True
            instance.save()
        return redirect('assets:employee_view')