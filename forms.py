from django import forms
from django.contrib.auth.models import User
from . import models

class NgoUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class NgoForm(forms.ModelForm):
    class Meta:
        model = models.Ngo
        fields = ['ngo_name', 'bloodgroup', 'address', 'mobile', 'profile_pic']

class DonationForm(forms.ModelForm):
    class Meta:
        model = models.BloodDonate
        fields = ['age', 'bloodgroup', 'disease', 'unit']
