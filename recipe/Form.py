from django import forms
from .choices import *

class FoodInput(forms.Form):
    vegetarien = forms.ChoiceField(label='Dietary characterization',choices=DIETARY_CHOICES)
