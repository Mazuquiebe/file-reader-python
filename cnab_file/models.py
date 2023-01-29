from django.db import models
import uuid


class CNABData(models.Model):

    id    = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type  = models.CharField(max_length=127)
    date  = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    cpf   = models.CharField(max_length=11)
    card  = models.CharField(max_length=16)
    owner = models.CharField(max_length=127)
    store = models.CharField(max_length=127) 


class CNABFile(models.Model):

    file = models.FileField(upload_to='uploads')