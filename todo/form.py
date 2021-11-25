from django import forms
from .models import Category
from django.core.validators import EmailValidator


class TodoForm(forms.Form):

    title = forms.CharField(max_length=200)
    details = forms.CharField(max_length=300)
    hasBeenDone = forms.BooleanField()
    date_creation = forms.DateField(help_text='Enter YYYY-DD-MM')
    date_completion = forms.DateField(help_text='Enter YYYY-DD-MM')
    deadline_date = forms.DateField(help_text='Enter YYYY-DD-MM')
    category = forms.ModelChoiceField(queryset=Category.objects.all())
