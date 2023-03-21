
from django.db import models
from django.utils import timezone


class Seg_Roles(models.Model):
    cod_roles = models.AutoField(primary_key=True, default=-1)
    tip_roles = models.CharField(max_length=20,default=-1)
    des_roles = models.CharField(max_length=50, default=-1)
    fec_modificacion = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'seg_roles'


