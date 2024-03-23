from django import forms
from django.core.exceptions import ValidationError

from .models import *

User = CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'username'
    }))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'password'
    }))


class Signup_form(forms.ModelForm):
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(

    ))

    class Meta:
        model = User
        fields = ("full_name", 'username', 'gmail', 'password', 'confirm_password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'email_input', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Parollar 1 hil emas ! Qayta urining.')
        return self.cleaned_data
