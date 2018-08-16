from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(required = True, label = 'Username', min_length= 4,  max_length = 32)
    email = forms.CharField(required = True, label = 'Email',min_length= 4,  max_length = 32)
    password = forms.CharField(required = True, label = 'Password', min_length= 4,  max_length = 32, widget = forms.PasswordInput())

class CadastroClienteForm(forms.Form):
    nome = models.CharField(required = True, label = 'Nome', max_length=56)
    telefone = models.CharField(required = True, label = 'Telefone', max_length=11)
    email = models.CharField(required = True, label = 'E-mail',max_length=256)