from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm

@login_required(login_url='/')
def painelUser(request):
    return render(request, 'controlpanel/painel.html', {})
# Create your views here.


def cadastro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        validForm = form.is_valid()
        if validForm:
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            userExists = User.objects.filter(username=username).exists()
            emailExists = User.objects.filter(email=email).exists()
            if userExists:
                form.add_error(None, "Usuário já cadastrado")
            elif emailExists:
                form.add_error(None, "Email já está em uso")
            validForm = form.is_valid()
            if validForm:
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'controlpanel/cadastro.html', {'form' : form})

#def listar_clientes(request):

