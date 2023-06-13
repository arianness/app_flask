-------------------------------------------------------------------------
EXECUTANDO API LOCALMENTE
-------------------------------------------------------------------------
Para executar a aplicação localmente, utilize um container do Docker.

Siga os passos para gerar e executar o container no diretório do 
arquivo Dockerfile: 

1. Gerando o Container: 
	 $ docker image build -t api-python .

2. Executando o Container:
	$ docker run -p 5001:5000 -d api-python

3. Acesse a url http://localhost:5001 via POSTMAN 
   (ou outra aplicação desejada) para interagir com a API
-------------------------------------------------------------------------
TESTES DE UNIDADE
-------------------------------------------------------------------------

Para rodar os testes implementados, você pode acessar o terminal 
do container e executar o seguinte comando: 
	
	$ python -m unittest

-------------------------------------------------------------------------
ENDPOINTS DISPONÍVEIS
-------------------------------------------------------------------------
Os seguintes endpoints são disponibilizados pela API:


**Endpoint**: /users/<user_id>

	Método: GET

	Descrição: Retorna o papel do usuário informado pelo id (user_id).



**Endpoint**: /users

	Método: POST

	Descrição: Cria um novo usuário na base de dados.
	

Campos obrigatórios: {"name": String, "email": String, "role": String}

Campos não obrigatórios: {"password": String}

-------------------------------------------------------------------------

-------------------------------------------------------------------------
