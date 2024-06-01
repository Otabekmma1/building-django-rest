from .models import *

from rest_framework import serializers

class HududSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hudud
        fields = '__all__'


class QurilishTashkilotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = QurilishTashkiloti
        fields = '__all__'


class QurilishBinosiSerializer(serializers.ModelSerializer):
    class Meta:
        model = QurilishBinosi
        fields = '__all__'