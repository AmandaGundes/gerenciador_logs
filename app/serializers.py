from rest_framework import serializers
from .models import Log

class LogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['descricao', 'origem', 'data_registro', 'level', 'usuario', 'tipo', 'eventos', 'detalhes']