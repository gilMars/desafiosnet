Aplicação desenvolvida utilizando os frameworks Django e Bootstrap.

1)

no arquivo urls.py no diretório raiz da aplicação, vá nas seguintes linhas:

SOCIAL_AUTH_FACEBOOK_KEY = ''  # Coloque aqui o seu App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '' # Coloque aqui a sua chave secreta

2)

OBS: Supondo que você já tenha o django instalado

execute o seguintes comandos

acesse o diretório raiz da aplicação:

python manage.py migrate
python manage.py runserver

e acesse o link http://localhost:8000