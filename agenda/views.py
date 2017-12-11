
from .models import Agendamento
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

        pprint(paciente)

        agendamento = Agendamento(paciente=paciente, data=data, hora_init=hora_init, procedimento=procedimento,
                                  hora_fin=hora_fin)
        agendamento.save()

        return HttpResponse('funcionou')

    else:
        return HttpResponse('Falhou')


@csrf_exempt
def read(request, id=None):

    #Pra mostrar todos os usuarios
    if (request.method=='GET'):

        todos = Agendamento.objects.all()

        #O resultado devera aparecer no terminal de onde o servidor Django esta rodando
        return HttpResponse(pprint(todos))

    #Pra mostrar usuario especifico
    elif(request.method=='POST'):

        #faaa uma insercao manual de id
        id = request.POST.get('id')
        resultado = Agendamento.objects.get(id=id)
        return HttpResponse('Seu usuario e: '+str(resultado))

    else:
        return HttpResponse('Falhou')

@csrf_exempt
def delete(request, id=None):

    if (request.method=='DELETE'):

        id = request.POST.get('id')
        paciente_deletado = Agendamento.objects.get(id=id)
        paciente_deletado.delete()

        return HttpResponse('Deletado!')
    else:
        return HttpResponsesCode()



class HttpResponsesCode(HttpResponse):
    NotFound = 404