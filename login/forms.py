from django import forms

class ClassForm(forms.Form):
    semester = forms.CharField(max_length=100)
    department = forms.CharField(max_length=100)
    instructor = forms.CharField(max_length=100)

class profileForm(forms.Form):
    studentID = forms.CharField(max_length=200)
    major = forms.CharField(max_length=200)
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
