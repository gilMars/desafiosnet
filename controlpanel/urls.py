from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginAuth, name='loginAuth'),
    path('cadastro/', views.registerUser, name='registerUser'),
    path('painel/', views.painelUser, name='painelUser'),
]