from django import forms
from .models import Course


class SearchForm(forms.Form):
    q = forms.CharField(required=False, label='')
