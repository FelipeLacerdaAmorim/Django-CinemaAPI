from rest_framework import serializers

from .models import Sala, SalaFilme, Filme

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

class SalaFilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaFilme
        fields = '__all__'

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'