from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput)