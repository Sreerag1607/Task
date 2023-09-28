from django import forms
from .models import District,Branch

class MyForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all())
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(),required=False)

class BranchForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select District")
    branch = forms.ModelChoiceField(queryset=Branch.objects.none(), empty_label="Select Branch")