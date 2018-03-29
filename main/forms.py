from django import forms
from .models import Provinces


class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Provinces
        fields = ['minister_name', 'capital', 'districts']


