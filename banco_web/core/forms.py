from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class UserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': _('Email')}
        )
    )

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': _('First Name')}
        )
    )

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': _('Last Name')}
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password')
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Confirm your password')
            }
        )
    )

    avatar = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'placeholder': _('Avatar')
            }
        )
    )

    class Meta:
        model = models.User
        fields = (
            'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar'
        )
