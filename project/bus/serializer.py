from .models import Bus
from rest_framework import  serializers

class BusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bus
		fields = '__all__'