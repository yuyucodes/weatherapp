from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'city-input',
                'placeholder': 'e.g. Tokyo',
                'autocomplete': 'off',
                'aria-label': 'City name',
            }),
        }