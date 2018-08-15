from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(required = True, label = 'Username', min_length= 4,  max_length = 32)
    email = forms.CharField(required = True, label = 'Email',min_length= 4,  max_length = 32)
    password = forms.CharField(required = True, label = 'Password', min_length= 4,  max_length = 32, widget = forms.PasswordInput())