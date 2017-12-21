from django import forms
from .choices import *

class FoodInput(forms.Form):
    vegetarien = forms.ChoiceField(label='Dietary characterization', choices=DIETARY_CHOICES)
    vegetables = forms.CharField(label='Vegetables',
                                 widget=forms.TextInput(attrs={
                                    'placeholder': 'Onion, Bell pepper',
                                    'value': 'Onion, Bell pepper'
                                 }))
    meat = forms.CharField(label='Meat',
                           widget=forms.TextInput(attrs={
                                    'placeholder': 'Minced meat, Chickenbreast',
                                    'value': 'Minced meat, Chickenbreast'
                           }))
