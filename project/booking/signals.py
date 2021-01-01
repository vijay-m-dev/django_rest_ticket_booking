from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from passengers.models import Passenger
from .models import Booking

@receiver(post_save,sender=Booking)
def booking_passenger_set(sender, instance, created, **kwargs):
	if created:
		for i in instance.passenger:
			name=i["name"]
			email=i["email"]
			phone=i["phone"]
			passenger=Passenger(name=name,email=email,phone=phone,booking=instance)
			passenger.save()
			print(passenger.booking)
		bus=instance.bus
		bus.available_seats-=instance.no_of_tickets
		bus.save()

@receiver(pre_delete,sender=Booking, dispatch_uid='bus_delete_signal')
def bus_tickets_update(sender, instance, using, **kwargs):
	bus=instance.bus
	bus.available_seats+=instance.no_of_tickets
	bus.save()

