from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def loginAuth(request):
    return render(request, 'controlpanel/login.html', {})

def registerUser(request):
    return render(request, 'controlpanel/cadastro.html', {})

@login_required(login_url='/')
def painelUser(request):
    return render(request, 'controlpanel/painel.html', {})
# Create your views here.
