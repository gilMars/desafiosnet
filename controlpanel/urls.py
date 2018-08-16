from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [


    path('painel/', views.painelUser, name='listar'),

    # Cadastrar clientes
    path('painel/cadastrar', views.cadastrar_cliente, name='cadastrar'),

    # URL para página de login costumizada
    path('', auth_views.login, {'template_name': 'controlpanel/login.html'}, name='login'),

    # URL para logout
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    
    # Autenticação por rede social
    path('oauth/', include('social_django.urls', namespace='social')),

    path('registrar/', views.registrar, name='registrar')
]