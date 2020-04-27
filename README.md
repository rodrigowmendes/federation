# Federation

Uma API REST de membros da Frota Estelar.

## Uso: 

Clone o repositório:

`$ git clone https://github.com/rodrigowmendes/federation.git`


Mude de diretório:

`$ cd federation`


Crie o arquivo com as variáveis de ambiente e altere-o como desejado:

`$ cp .env.example .env`


Suba o ambiente (necessário Docker e docker-compose instalados):
`$ docker-compose up -d`


Crie o banco de dados:

`$ docker-compose run web python3 manage.py migrate` 


Crie um superusuário:

`$ docker-compose run web python3 manage.py createsuperuser`


Vida longa e próspera!  


