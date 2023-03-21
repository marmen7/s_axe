from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from .models import Seg_Roles

class AXESeriealizers(serializers.ModelSerializer):
    class Meta:
        model = Seg_Roles
        fields = '__all__'