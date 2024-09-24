# birthdate/views.py
from django.shortcuts import render
from datetime import datetime
from .forms import BirthdateForm

def calculate_age(birth_date):
    today = datetime.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += (birth_date.replace(month=birth_date.month + 1, day=1) - birth_date).days
    
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def age_view(request):
    age_result = None
    if request.method == 'POST':
        form = BirthdateForm(request.POST)
        if form.is_valid():
            birth_date = form.cleaned_data['birth_date']
            years, months, days = calculate_age(birth_date)
            age_result = f'You are {years} years, {months} months, and {days} days old.'
    else:
        form = BirthdateForm()

    return render(request, 'birthdate/age.html', {'form': form, 'age_result': age_result})
