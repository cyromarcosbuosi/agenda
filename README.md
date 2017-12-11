# agenda



Documentação:


Primeiramente, para que o projeto possa rodar você vai precisar de uma ferramenta de teste.

Neste projeto eu usei o Postman, sugiro que faça o mesmo.

https://www.getpostman.com/apps


Entre neste link e baixe a versão Linux. Extraia o arquivo .gz 
Abra um terminal com endereço do diretório e digite ./Postman
O Postman deverá abrir logo em seguida.

Agora que você esta no Postman, para testar cada função REST você deve 
colocar o endereço específico de cada função e seu metodo request respectivo
e o corpo Json com os dados a serem enviados.

Aqui vão os exemplos que utilizei:

POST
 adiciona usuário
 localhost:8000/agenda/add
 
 {
		"paciente": "Cyro Marcos",
		"data": "2012-04-23T18:25:43.511Z",
		"hora_init": "17:30",
		"hora_fin": "18:30",
		"procedimento": "O paciente tem problemas"
	}
  
  retorna usuário especifico
  localhost:8000/agenda/read
  {
		"id": 1
	}
 
GET
  retorna todos os usuários
  localhost:8000/agenda/add
  
PUT
  altera usuário existente
  localhost:8000/agenda/alter
  
  {
		"id": 1,
		"paciente": "Luiz Eduardo",
		"data": "2014-03-23T18:25:43.511Z",
		"hora_init": "17:30",
		"hora_fin": "18:30",
		"procedimento": "O paciente tem problemas"
	}

DELETE
  deleta usuário pelo id
  localhost:8000/agenda/delete

  {
		"id": 1
	}
  
LISTA DE DEPENDÊNCIAS DE PACOTES:

from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json
