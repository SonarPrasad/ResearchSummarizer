from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',  # Replace with your actual class name
        'placeholder': 'Enter your email'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',  # Replace with your actual class name
                'placeholder': 'Enter your username'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',  # Replace with your actual class name
                'placeholder': 'Enter your password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',  # Replace with your actual class name
                'placeholder': 'Confirm your password'
            }),
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',  # Replace with your actual class name
                'placeholder': 'Enter your username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',  # Replace with your actual class name
                'placeholder': 'Enter your password'
            }),
        }