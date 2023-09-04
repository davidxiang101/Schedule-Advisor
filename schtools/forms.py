from django import forms

class ScheduleForm(forms.Form):
    name = forms.CharField(max_length=100)

