from django.db import models
from postManager.models import PostBase

# Create your models here.


class Ticket(models.Model):
	ticket_descrption = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	post_id = models.ForeignKey('postManager.PostBase')

	def __unicode__(self):
		if self.ticket_descrption:
			return u'%s:%s' % (self.ticket_descrption, self.price)

