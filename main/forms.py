from django import forms
from .models import Event

class EventCreationForm(forms.ModelForm):
    date = forms.DateField(label="Podaj datę", widget=forms.TextInput(attrs={'type': 'date'}))
    description = forms.CharField(label="Dodatkowe informacje")
    class Meta:
        model = Event
        fields = ('date', 'description')
