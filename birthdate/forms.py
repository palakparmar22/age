# birthdate/forms.py
from django import forms

class BirthdateForm(forms.Form):
    birth_date = forms.DateField(
        label='Enter your birth date',
        widget=forms.TextInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Select birth date'}),
        input_formats=['%d/%m/%Y'],
    )
