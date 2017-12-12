import json
from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Agendamento
from rest_framework.response import Response

# Create your views here.

jsonResponse = {}
jsonResponse['resultado'] = 'Sucesso'
jsonResponse['mensagem'] = 'Requisicao feita com sucesso!'

jsonBadResponse = {}
jsonBadResponse['resultado'] = 'Erro'
jsonBadResponse['mensagem'] = 'Requisicao nao executada'



@csrf_exempt
def add(request):
    if (request.method == 'POST'):

        jload = json.loads(request.body.decode("utf-8"))

        paciente = jload[""u'paciente'""]
        data = jload[""u'data'""]
        hora_init = jload[""u'hora_init'""]
        hora_fin = jload[""u'hora_fin'""]
        procedimento = jload[""u'procedimento'""]

        if (Response.status_code == 200):
            agendamento = Agendamento(paciente=paciente, data=data, hora_init=hora_init, procedimento=procedimento,
                                      hora_fin=hora_fin)
            agendamento.save()

            return HttpResponse(json.dumps(jsonResponse))

        else:
            return HttpResponse(json.dumps(jsonBadResponse))


@csrf_exempt
def read(request, id=None):
    # Pra mostrar todos os usuarios
    if (request.method == 'GET'):

        todos = Agendamento.objects.all()


        return HttpResponse(todos)

    # Pra mostrar usuario especifico
    elif (request.method == 'POST'):
        jload = json.loads(request.body.decode("utf-8"))
        # faca uma insercao manual de id
        id = jload[""u'id'""]
        resultado = Agendamento.objects.filter(id=id, ).values()
        return HttpResponse('Seu usuario e: ' + str(resultado))

    else:
        return HttpResponse(json.dumps(jsonBadResponse))


@csrf_exempt
def delete(request, id=None):
    if (request.method == 'DELETE'):

        jload = json.loads(request.body.decode("utf-8"))
        id = jload[""u'id'""]

        if (Agendamento.objects.filter(id=id).exists()):
            resultado = Agendamento.objects.get(id=id)
            resultado.delete()
            return HttpResponse('Funcionou!')
        else:
            return HttpResponse('Ele ja nao existia antes')
    else:
        return HttpResponse('falhou')


@csrf_exempt
def alter(request, id=None):
    if (request.method == 'PUT'):
        jload = json.loads(request.body.decode("utf-8"))

        paciente = jload[""u'paciente'""]
        data = jload[""u'data'""]
        hora_init = jload[""u'hora_init'""]
        hora_fin = jload[""u'hora_fin'""]
        procedimento = jload[""u'procedimento'""]
        id = jload[""u'id'""]

        if (Agendamento.objects.filter(id=id).exists()):

            Agendamento.objects.filter(id=id).update(paciente=paciente, data=data, hora_fin=hora_fin,
                                                     hora_init=hora_init,
                                                     procedimento=procedimento, data_alteracao=datetime.now())

            return HttpResponse('Funcionou!')
        else:
            return HttpResponse('Usuario nao encontrado')
    else:
        return HttpResponse('falhou')
