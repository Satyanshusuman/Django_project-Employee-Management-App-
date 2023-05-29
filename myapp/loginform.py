from django import forms
from emp.models import Employee


class Loginform(forms.Form):
   username=forms.CharField(max_length=50)
   password=forms.CharField(widget=forms.PasswordInput)
