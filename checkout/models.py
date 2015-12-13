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

# class userStripe(models.Model):
# 	user = models.OneToOneField(settings.AUTH_USER_MODEL)
# 	stripe_id = models.CharField(max_length=200, null=True, blank=True)

# 	def __unicode__(self):
# 		if self.stripe_id:
# 			return str(self.stripe_id)
# 		else:
# 			return self.user.username


class PurchaseDetails(models.Model):
	user = models.ForeignKey('accounts.MyUser',null=True)
	post_id = models.ForeignKey('postManager.PostBase',null=True)
	amount_price = models.DecimalField(max_digits=8, decimal_places=2,null=True)
	amount_items = models.IntegerField(null=True)

	def __unicode__(self):
		return u'%s: %s' % (self.user, self.post_id)



# Retrieve purchase history from stripe and save to the DB
# def purchaseCallback(sender, request, user, **kwargs):
#     user_stripe_account, created = userStripe.objects.get_or_create(user=user)
#     if created:
#         print 'created for %s'%(user.email)

#     if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
#         new_stripe_id = stripe.Customer.create(email = user.email)
#         user_stripe_account.stripe_id = new_stripe_id['id']
#         user_stripe_account.save()

# request_finished.connect(purchaseCallback)


	

		