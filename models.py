#from django.db import models

# Create your models here.
#cod recomender
from datetime import timezone
from django.db import models  
from django.utils import timezone

class Person_Emailes(models.Model):
    cod_email = models.IntegerField(primary_key=True, default=-1)
    dir_correo = models.CharField(max_length=50, default=-1)
    des_correo = models.CharField(max_length=50, default=-1)
    fec_creacion = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'person_emailes'

class Person_Telefonos(models.Model):
    cod_telefono = models.IntegerField(primary_key=True, default=-1)
    num_telefono = models.CharField(max_length=20, default=-1)
    tip_telefono = models.CharField(max_length=1, default=-1)

    class Meta:
        db_table = 'person_telefonos'
