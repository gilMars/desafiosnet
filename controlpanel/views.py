from django.shortcuts import render

# Anotação para autenticação
from django.contrib.auth.decorators import login_required

# Import para autenticação de cadastro de usuário como também de login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from .forms import CadastroClienteForm
from .forms import DeletarClienteForm
from .models import Cliente
from .models import Endereco


@login_required(login_url='/')
def painelUser(request):
    clientes = Cliente.objects.filter(user_id=request.user)
    return render(request, 'controlpanel/painel.html', {'clientes': clientes})


@login_required(login_url='/')
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST)
       # validForm = form.is_valid()
       # if validForm:
        form.is_valid()
        clienteObj = form.cleaned_data
        nome = clienteObj['nome']
        telefone = clienteObj['telefone']
        cep = clienteObj['cep']
        endereco = clienteObj['endereco']
        numero = clienteObj['numero']
        cidade = clienteObj['cidade']
        estado = clienteObj['estado']
        pais = clienteObj['pais']
        # clienteExists = Cliente.objects.filter(user_id=request.user,nome=nome).exists()
        # if userExists:
        # form.add_error(None, "Cliente já está cadastrado")
        # validForm = form.is_valid()
        # if validForm:
        cliente = Cliente(user_id=request.user, nome=nome, telefone=telefone)
        cliente.save()
        Endereco.objects.create(cliente_id=cliente, cep=cep, endereco=endereco,
                                cidade=cidade, numero=numero, estado=estado, pais=pais)
    else:
        form = CadastroClienteForm()
    return render(request, 'controlpanel/cadastrar.html', {'form': form})


def registrar(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        validForm = form.is_valid()
        if validForm:
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            userExists = User.objects.filter(username=username).exists()
            emailExists = User.objects.filter(email=email).exists()
            if userExists:
                form.add_error(None, "Usuário já cadastrado")
            elif emailExists:
                form.add_error(None, "Email já está em uso")
            validForm = form.is_valid()
            if validForm:
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'controlpanel/cadastro.html', {'form': form})


@login_required(login_url='/')
def deletar_cliente(request):
    clientes = Cliente.objects.filter(user_id=request.user)
    if request.method == 'POST':
        form = DeletarClienteForm(request.POST)
        if form.is_valid():
            Cliente.objects.filter(nome=form.cleaned_data['nome']).delete()
    else:
        form = DeletarClienteForm()
    return render(request, 'controlpanel/deletar.html', { 'form':form, 'clientes':clientes })
