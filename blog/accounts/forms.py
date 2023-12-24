from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreation(UserCreationForm):

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

class UserEdition(UserChangeForm):

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )
    
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    avatar = forms.ImageField(
        label="Avatar",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'form3Example5'})
    )

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "password1", "password2", "avatar"]
        help_text = {k: "" for k in fields}