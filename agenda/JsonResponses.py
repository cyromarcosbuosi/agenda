from rest_framework import status
from django.http import HttpResponse
import json
def successful():
    jsonResponse = {
		'resultado': "Suceosso!",
        'mensagem':'requisicao feita com sucesso!'
	}
    jsonResponse = json.dumps(jsonResponse)
    return HttpResponse(jsonResponse, status=status.HTTP_200_OK)

def notSuccessful():
    jsonResponse = {
        'resultado': 'Erro!',
        'mensagem': 'Algo que voce fez nao esta correto!'
    }
    jsonResponse = json.dumps(jsonResponse)
    return HttpResponse(jsonResponse, status=status.HTTP_400_BAD_REQUEST)


def BadRequest():
    jsonResponse = {
        'resultado': 'Erro!',
        'mensagem': 'Requisicao nao suportada!'
    }
    jsonResponse = json.dumps(jsonResponse)
    return HttpResponse(jsonResponse, status=status.HTTP_400_BAD_REQUEST)

def NotFound():
    jsonResponse = {
        'resultado': 'Erro!',
        'mensagem': 'A requisicao enviada nao pode ser completa pois o que foi requisitado nao existe!'
    }
    jsonResponse = json.dumps(jsonResponse)
    return HttpResponse(jsonResponse, status=status.HTTP_404_NOT_FOUND)

def InternalError():
    jsonResponse = {
        'resultado': 'Erro!',
        'mensagem': 'Ops! Algo deu errado nos nossos servidores!'
    }
    jsonResponse = json.dumps(jsonResponse)
    return HttpResponse(jsonResponse, status=status.HTTP_500_INTERNAL_SERVER_ERROR)