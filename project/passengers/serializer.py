from rest_framework import  serializers
from .models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Passenger
        fields = ["name","email","phone"]

class Passenger1Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Passenger
        fields = "__all__"