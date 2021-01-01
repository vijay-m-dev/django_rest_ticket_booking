from .models import Booking
from passengers.serializer import PassengerSerializer
from rest_framework import  serializers


class BookingSerializer(serializers.ModelSerializer):
	passenger=PassengerSerializer(many=True)
	class Meta:
		model = Booking
		fields = '__all__'

class Booking1Serializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = '__all__'