from django.db import models
from postManager.models import PostBase
from accounts.models import MyUser
from django.core.signals import request_finished

# from django.conf import settings
# import stripe


# Create your models here.


class Ticket(models.Model):
	ticket_descrption = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	post_id = models.ForeignKey('postManager.PostBase')

	def __unicode__(self):
		if self.ticket_descrption:
			return u'%s:%s' % (self.ticket_descrption, self.price)


class PurchaseDetails(models.Model):
	user = models.ForeignKey('accounts.MyUser',null=True)
	post_id = models.ForeignKey('postManager.PostBase',null=True)
	amount_price = models.DecimalField(max_digits=8, decimal_places=2,null=True)
	amount_items = models.IntegerField(null=True)

	def __unicode__(self):
		return u'%s: %s' % (self.user, self.post_id)