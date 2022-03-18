from dataclasses import field, fields
from rest_framework import serializers
from registros.models import Objeto, Localizacao

class ObjetoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = '__all__'

class LocalizacaoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__' 

"""class ObjetoLocalizacaoSerializer (serializers.ModelSerializer):
    class Meta:
        model = ObjetoLocalizacao
        fields = '__all__'                

class ListaObjetoSerializer (serializers.ModelSerializer):
    estadoNacao = serializers.ReadOnlyField(source = "objeto.estadoNacao")
    numeroDeOrdem = serializers.SerializerMethodField()

    def get_numeroDeOrdem (self, obj):
        return obj.get_numeroDeOrdem_display()

    class Meta:
        model = ObjetoLocalizacao
        fields = '__all__'
"""