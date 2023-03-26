from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from .models import Person_Emailes, Person_Telefonos

class EmailesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person_Emailes
        fields = '__all__'

class TelefonosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person_Telefonos
        fields = '__all__'