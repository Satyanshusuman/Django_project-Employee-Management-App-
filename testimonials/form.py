from django import forms
from.models import Feedback


class Feedbackform(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"
        widgets={
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "feedback":forms.Textarea(attrs={"class":"form-control"}),}
    def clean_name(self):
        valname=self.cleaned_data.get("name")    
        if len(valname)<4:
            raise forms.ValidationError("enter morethan 4 char")
        return valname