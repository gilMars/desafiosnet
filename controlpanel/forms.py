from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(required = True, label = 'Username', min_length= 4,  max_length = 32)
    email = forms.CharField(required = True, label = 'Email',min_length= 4,  max_length = 32)
    password = forms.CharField(required = True, label = 'Password', min_length= 4,  max_length = 32, widget = forms.PasswordInput())

class CadastroClienteForm(forms.Form):
    nome = forms.CharField(required = True, max_length=56)
    telefone = forms.CharField(required = True, max_length=11)
    cep = forms.CharField(required = True, max_length=8)
    endereco = forms.CharField(max_length=512)
    cidade = forms.CharField(max_length=512)
    numero = forms.IntegerField()
    estado = forms.CharField(max_length=256)
    pais = forms.CharField( max_length=256)

class DeletarClienteForm(forms.Form):
    nome = forms.CharField(required = True, max_length=56)

class ModificarClienteForm(forms.Form):
    id = forms.CharField(required = True)
    nome = forms.CharField(required = True, max_length=56)
    telefone = forms.CharField(required = True, max_length=11)
    cep = forms.CharField(required = True, max_length=8)
    endereco = forms.CharField(max_length=512)
    cidade = forms.CharField(max_length=512)
    numero = forms.IntegerField()
    estado = forms.CharField(max_length=256)
    pais = forms.CharField( max_length=256)