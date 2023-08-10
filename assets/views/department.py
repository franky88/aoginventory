from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from assets.forms.department import DepartmentForm
from assets.models.employee import Department
from django.views.decorators.http import require_POST

def department_view(request):
    form = DepartmentForm(request.POST or None)
    departments = Department.objects.all()
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('assets:department_list')
    context = {
        "title": "departments",
        "form": form,
        "departments": departments
    }
    return render(request, 'departments/list.html', context)

def department_view_details(request, pk):
    instance = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('assets:department_view_details', pk=obj.pk)
    context = {
        "title": "update department",
        "form": form,
        "instance": instance
    }
    return render(request, 'departments/details.html', context)

@require_POST
def department_view_delete(request, pk):
    instance = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        instance.delete()
        return redirect('assets:department_list')