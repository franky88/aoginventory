from django import forms
from assets.models.employee import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'employee_id',
            'full_name',
            'email',
            'contact_number',
            'department'
        ]