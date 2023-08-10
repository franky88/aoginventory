from django import forms
from assets.models.employee import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'name'
        ]