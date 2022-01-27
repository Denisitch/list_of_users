from django import forms
from users.models import Users


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = (
            "first_name",
            "last_name",
            "patronymic",
            "date_of_birth",
            "phone_number",
            "status",
            "photo",
        )
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "patronymic": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_birth": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }
