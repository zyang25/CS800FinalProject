from django.db import models
from postManager.models import PostBase
# from accounts.models import MyUser
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

# class userStripe(models.Model):
# 	user = models.OneToOneField(settings.AUTH_USER_MODEL)
# 	stripe_id = models.CharField(max_length=200, null=True, blank=True)

# 	def __unicode__(self):
# 		if self.stripe_id:
# 			return str(self.stripe_id)
# 		else:
# 			return self.user.username
