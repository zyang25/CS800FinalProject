from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe

# stripe.api_key = settings.STRIPE_SECRET_KEY
# # Create your views here.
# @login_required(login_url='/')
# def checkout(request):
# 	publishKey = settings.STRIPE_PUBLISHABLE_KEY	
# 	if request.method == 'POST':
# 		token = request.POST['stripeToken']
# 		# Create the charge on Stripe's servers - this will charge the user's card
# 		try:

#   			charge = stripe.Charge.create(
#       			amount=1000, # amount in cents, again
#       			currency="usd",
#       			customer=token,
#       			description="payinguser@example.com"
#   				)
# 		except stripe.error.CardError, e:
#   			# The card has been declined
#   			pass
# 	context = {'publishKey': publishKey}
# 	template = 'details_tpl.html'
# 	return render(request, template, context)

# # Create your views here.
# @login_required(login_url='/')
# def checkout(request):
# 	user = request.user
# 	context = {'user': user}
# 	template = 'details_tpl.html'
# 	return render(request, template, context)

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required(login_url='/')
def checkout(request, activity_id):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.userstripe.stripe_id
	if request.method == 'POST':
		token = request.POST['stripeToken']
		print token
	# Create the charge on Stripe's servers - this will charge the user's card
		try:
		  # Associate card information to a customer_id
		  customer = stripe.Customer.retrieve(customer_id)
		  customer.sources.create(source=token)
		  charge = stripe.Charge.create(
      			amount=1000, # amount in cents, again
      			currency="usd",
      			customer=customer,
      			description="payinguser@example.com"
  				)
		except stripe.error.CardError, e:
		  # The card has been declined
		  pass
	context = {'publishKey':publishKey}
	template = 'details_tpl.html'
	return render(request, template, context)