from django.db import models
from django.utils import timezone
# Create your models here.

#Representa la tabla que tenemos en la BD
class seg_permisos(models.Model):
    cod_permisos = models.IntegerField(primary_key=True, default=-1)
    cod_rol = models.IntegerField()
    per_insercion = models.CharField(max_length=1, default=-1)
    per_eliminar = models.CharField(max_length=1, default=-1)
    per_actualizar = models.CharField(max_length=1, default=-1)
    per_consultar = models.CharField(max_length=1, default=-1)
    fec_modificacion = models.DateTimeField(default=timezone.now)
    
    #
    class Meta:
        db_table = 'seg_permisos'