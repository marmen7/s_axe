from rest_framework import serializers
from .models import seg_permisos

class PermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = seg_permisos
        fields = '__all__'