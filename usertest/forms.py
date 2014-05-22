from django import forms

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    email = forms.EmailField()

class UpdateForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

