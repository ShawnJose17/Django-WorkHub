from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User
import re


class RegisterForm(UserCreationForm):

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email',
            'phone', 'username', 'user_type',
            'password1', 'password2'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'phone': forms.TextInput(attrs={'required': True}),
            'user_type': forms.Select(attrs={'required': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].validators = []
        self.fields['password2'].validators = []

        self.fields['password1'].help_text = (
            "Password must contain: 1 uppercase, 1 lowercase, "
            "1 number, 1 special character, and at least 8 characters."
        )
        self.fields['password2'].help_text = ""

    def clean(self):
        cleaned_data = super().clean()

        required_fields = [
            "first_name", "last_name", "email",
            "phone", "username", "user_type",
            "password1", "password2"
        ]

        for field in required_fields:
            if not cleaned_data.get(field):
                raise ValidationError(f"{field.replace('_', ' ').title()} is required.")

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not email:
            raise ValidationError("Email is required.")

        if not email.endswith("@gmail.com"):
            raise ValidationError("Only @gmail.com email addresses are allowed.")

        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered. Please use a different email.")

        return email

    def clean_password1(self):
        password = self.cleaned_data.get("password1")

        if not password:
            raise ValidationError("Password is required.")

        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        if not re.search(r"[A-Z]", password):
            raise ValidationError("Password must contain at least one uppercase letter.")

        if not re.search(r"[a-z]", password):
            raise ValidationError("Password must contain at least one lowercase letter.")

        if not re.search(r"[0-9]", password):
            raise ValidationError("Password must contain at least one number.")

        if not re.search(r"[^A-Za-z0-9]", password):
            raise ValidationError("Password must contain at least one special character.")

        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not password2:
            raise ValidationError("Confirm Password is required.")

        if password1 != password2:
            raise ValidationError("Passwords do not match.")

        return password2

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username/Email",
        widget=forms.TextInput(attrs={'placeholder': 'Username/Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
