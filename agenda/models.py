from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils import formats

# Create your models here.


class Agendamento(models.Model):


    paciente = models.CharField(max_length= 150)
    data = models.DateTimeField(max_length=100)
    hora_init = models.TimeField(max_length=100)
    hora_fin = models.TimeField(max_length=100)
    procedimento = models.TextField(max_length=400)
    data_criacao = models.DateTimeField(default=datetime.now)
    data_alteracao = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.paciente
