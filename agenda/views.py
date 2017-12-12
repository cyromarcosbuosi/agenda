import json
from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Agendamento
from rest_framework.response import Response
from .Validator import dataValidator, horaFinValidator, horaInitValidator, pacienteValidator, procedimentoValidator
from . import JsonResponses
from rest_framework import status


# Create your views here.







@csrf_exempt
def add(request):
    if (request.method == 'POST'):

        jload = json.loads(request.body.decode("utf-8"))

        paciente = jload[""u'paciente'""]
        if pacienteValidator(paciente) == False:
            return HttpResponse((JsonResponses.notSuccessful()))

        data = jload[""u'data'""]
        if dataValidator(data) == False:
            return HttpResponse(json.dumps(JsonResponses.notSuccessful()))

        hora_init = jload[""u'hora_init'""]
        if horaInitValidator(hora_init) == False:
            return HttpResponse(json.dumps(JsonResponses.notSuccessful()))

        hora_fin = jload[""u'hora_fin'""]
        if horaFinValidator(hora_fin, hora_init) == False:
            return HttpResponse(json.dumps(JsonResponses.notSuccessful()))

        procedimento = jload[""u'procedimento'""]
        if procedimentoValidator(procedimento) == True:
            return HttpResponse(json.dumps(JsonResponses.notSuccessful()))

        if (Response.status_code == 200):
            agendamento = Agendamento(paciente=paciente, data=data, hora_init=hora_init, procedimento=procedimento,
                                      hora_fin=hora_fin)
            agendamento.save()

            return HttpResponse(JsonResponses.successful(), status=status.HTTP_201_CREATED)
        elif(Response.status_code==500):
            return HttpResponse(JsonResponses.InternalError())

        else:
            return HttpResponse(JsonResponses.BadRequest())


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

        if resultado.exists():
            return HttpResponse('Seu usuario e: ' + str(resultado))

        else:
            return  HttpResponse(JsonResponses.NotFound())


    else:
        status = Response.status_code
        return HttpResponse(JsonResponses.NotFound())


@csrf_exempt
def delete(request, id=None):
    if (request.method == 'DELETE'):

        jload = json.loads(request.body.decode("utf-8"))
        id = jload[""u'id'""]

        if (Agendamento.objects.filter(id=id).exists()):
            resultado = Agendamento.objects.get(id=id)
            resultado.delete()
            return HttpResponse(JsonResponses.successful())
        else:
            return HttpResponse(JsonResponses.NotFound())
    else:
        return HttpResponse(JsonResponses.BadRequest())


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

            return HttpResponse(JsonResponses.successful())
        else:
            return HttpResponse(JsonResponses.NotFound())
    else:
        return HttpResponse(JsonResponses.BadRequest())
