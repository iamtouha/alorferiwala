from django import forms

class RegisterForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    phone_no = forms.CharField(max_length=14)
    address = forms.CharField(max_length=255)
    picture = forms.ImageField(max_length=255, required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)