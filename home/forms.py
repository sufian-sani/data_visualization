from django import forms
from .models import *

class UpdateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=jsonModel
        exclude = ('id',)