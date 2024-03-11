from django import forms
from .models import Employee


class AddEmployeeForm(forms.ModelForm):
    # Syntax for form fields is Field_name = forms.FieldType(attributes)
    first_name = forms.CharField(
        required=True,
        label="",
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )

    last_name = forms.CharField(
        required=True,
        label="",
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )

    email = forms.CharField(
        required=True,
        label="",
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )

    class Meta:
        # setting model as Employee model defined in models.py
        model = Employee
        # include all fields
        fields = "__all__"
