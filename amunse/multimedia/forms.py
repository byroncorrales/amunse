from django import forms
from models import *

class AdjuntaForm(forms.ModelForm):
    class Meta:
        model = ImagenAdjunta


