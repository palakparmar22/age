from django.urls import path
from . import views

urlpatterns = [
    path('', views.age_view, name='age_calculator'),
]
