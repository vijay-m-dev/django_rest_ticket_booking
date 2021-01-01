from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from bus.models import Bus
# Create your models here.
class Booking(models.Model):
	user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
	bus = models.ForeignKey(Bus, on_delete= models.CASCADE)
	no_of_tickets = models.PositiveIntegerField(validators=[MinValueValidator(1)])
	total_cost = models.PositiveIntegerField(validators=[MinValueValidator(1)],null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def compute_total_cost(self):
		total_cost=self.no_of_tickets*self.bus.price
		return total_cost

	def save(self, *args, **kwargs):
		self.total_cost=self.compute_total_cost()
		super(Booking, self).save(*args, **kwargs)

	def __str__(self):
		return 'booking'+str(self.id)

	