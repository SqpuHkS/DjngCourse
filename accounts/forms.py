from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Input username'
    }))

    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Input password'
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise ValidationError('This username does not exist')
            if not check_password(password, qs[0].password):
                raise ValidationError('Password is not correct')
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError('This user is inactive')
        return super().clean(*args, **kwargs)