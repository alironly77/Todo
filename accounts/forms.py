from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=64)
    password = forms.CharField(max_length=16)
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length= 32)
    password = forms.CharField(max_length=16)

