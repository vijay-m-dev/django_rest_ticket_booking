from django.db import models
from booking.models import Booking
# Create your models here.

class Passenger(models.Model):
	booking = models.ForeignKey(Booking, on_delete= models.CASCADE)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	
	def __str__(self):
		return self.name