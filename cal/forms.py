from django import forms

class ClassForm(forms.Form):
    semester = forms.CharField(max_length=100)
    department = forms.CharField(max_length=100)
    instructor = forms.CharField(max_length=100)
