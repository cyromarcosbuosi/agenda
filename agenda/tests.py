import pprint
from django.test import TestCase
from datetime import datetime
# Create your tests here.
from .models import Agendamento
import requests
# from urllib.request import , urlopen
import json



def test():
    data = datetime.now
    dados = {'paciente': 'Teste', 'data': data, 'hora_init': data, 'procedimento': 'Procedimento teste',
             'hora_fin': 'data'}
    dados = json.dumps(dados)
    r = requests.post('localhost/agenda/add', dados)



