from rest_framework import serializers
from . models import Car, AirCraft, Ship

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        
class AirCraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirCraft
        fields = '__all__'
        
        
class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = '__all__'