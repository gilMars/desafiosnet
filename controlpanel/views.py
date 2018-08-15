from django.shortcuts import render

def loginAuth(request):
    return render(request, 'controlpanel/login.html', {})

def registerUser(request):
    return render(request, 'controlpanel/cadastro.html', {})

def painelUser(request):
    return render(request, 'controlpanel/painel.html', {})

# Create your views here.
