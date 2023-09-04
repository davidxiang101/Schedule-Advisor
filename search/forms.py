from django import forms

class ClassForm(forms.Form):
    subject = forms.CharField(max_length=200)
    descr = forms.CharField(max_length=200) 
    catalog_nbr = forms.IntegerField()

class ClassInfoForm(forms.Form):
    subject = forms.CharField(max_length=200)
    catalog_nbr = forms.IntegerField()
    crse_id = forms.IntegerField()
    class_section = forms.IntegerField()
    descr = forms.CharField(max_length=200) 
    days = forms.CharField(max_length=200) 
    start_time = forms.CharField(max_length=200) 
    end_time = forms.CharField(max_length=200) 