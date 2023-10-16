from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from auth_user.views import validate_age
from hotel.models import Client


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'input-1'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'input-1'}))
    patronymic = forms.CharField(label='Patronymic', widget=forms.TextInput(attrs={'class': 'input-1'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'input-1'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input-1'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'input-1'}))
    password2 = forms.CharField(label='Password replay', widget=forms.PasswordInput(attrs={'class': 'input-1'}))

    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'input-1'}),
        label='Birth date', validators=[validate_age])

    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '+375 (XX) XXX-XX-XX', 'class': 'input-1'}),
        max_length=20,
        required=False,
        help_text='Format: +375 (XX) XXX-XX-XX',
        label='Phone number',
        validators=[RegexValidator(regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$',
                                   message='Phone number must be in the format +375 (XX) XXX-XX-XX')])

    class Meta(UserCreationForm.Meta):
        model = Client
        fields = ('first_name',
                  'last_name',
                  'patronymic',
                  'birth_date',
                  'phone_number',
                  'username',
                  'email',
                  'password1',
                  'password2',)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'input-1'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'input-1'}))
