from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.


class Agendamento(models.Model):

    paciente = models.CharField(max_length= 150, null=True, blank=True)
    data = models.DateTimeField(max_length=100, null=True, blank=True)
    hora_init = models.TimeField(max_length=100, null=True, blank=True)
    hora_fin = models.TimeField(max_length=100, null=True, blank=True)
    procedimento = models.TextField(max_length=400, null=True, blank=True)
    data_criacao = models.DateTimeField(default=datetime.now, null=True, blank=True)
    data_alteracao = models.DateTimeField(default=datetime.now, null=True, blank=True)


    def __str__(self):
        return self.pat_Name