from rest_framework import serializers
from .models import Temperature

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['temperature', 'humidity']

class TemperatureDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['temperature', 'humidity', 'timestamp']