from django import forms



class Loginform(forms.Form):
   username=forms.CharField(max_length=50)
   password=forms.CharField(widget=forms.PasswordInput)
