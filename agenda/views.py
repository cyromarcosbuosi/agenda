from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from django.contrib import messages
from pprint import  pprint
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def add(request):

    if (request.method == 'POST'):

        paciente = request.POST.get('paciente')
        data = request.POST.get('data')
        hora_init = request.POST.get('hora_init')
        hora_fin = request.POST.get('hora_fin')
        procedimento = request.POST.get('procedimento')

        agendamento = Agendamento(paciente=paciente, data=data, hora_init=hora_init, procedimento=procedimento,
                                  hora_fin=hora_fin)
        agendamento.save()

        return HttpResponse('Salvo')

    else:
        return HttpResponse('Falhou')