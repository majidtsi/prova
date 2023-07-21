from django import forms
from django.contrib.auth.models import User
from .models import Reservation, Piatti


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class PrenotaForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class OrdineForm(forms.ModelForm):
    class Meta:
        model = Piatti
        fields = '__all__'










