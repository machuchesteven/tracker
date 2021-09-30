from django import forms
from .models import *

class TrialForm(forms.Form):
    name = forms.CharField()

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"