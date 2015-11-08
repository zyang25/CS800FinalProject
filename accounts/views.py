#Django
from django.conf import settings
from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.context_processors import csrf
from django.views.generic.base import TemplateView
from django.template import Context, loader
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
#Models
from .models import MyUser, UserActivation
#Forms
from .forms import SignUpForm, LoginForm
#Email
import hashlib, datetime, random

# Create your views here.

def account_index(request):
	
	signup = SignUpForm(request.POST or None)
	login = LoginForm(request.POST or None)

	context = {
	'signupform': signup,
	'loginform':login,
	}
	context.update(csrf(request))

	print request.POST

	if request.method == 'POST':
		if 'emailcheck' in request.POST:
			emailcheck = request.POST.get('emailcheck', False)
			u = MyUser.objects.filter(email=emailcheck).count()
			if u !=0:
				res = "Bad";
				print "BAD"
			else:
				res = "OK"
				print "OK"
			return HttpResponse(res)

		if 'signup_submit' in request.POST:
			if signup.is_valid():
				print 'You are in signup post'
				signup.save()
				# Key salt
				email = signup.cleaned_data['email']
				salt = hashlib.sha1(str(random.random())).hexdigest()[:5]            
				activation_key = hashlib.sha1(salt+email).hexdigest()            
				key_expires = datetime.datetime.today() + datetime.timedelta(2)

				#Get user by email
				user=MyUser.objects.get(email=email)

				# Create and save user profile                                                                                                                                  
				new_profile = UserActivation(user=user, activation_key=activation_key, 
				key_expires=key_expires)
				new_profile.save()

				# Send email with activation key
				email_subject = 'Wejoin Account Confirmation'
				email_body = "Hello %s, thanks for signing up. To activate your account, click this link within \
				48hours http://127.0.0.1:8000/accounts/confirm/%s" % (email, activation_key)
				from_email = settings.EMAIL_HOST_USER
				to_list = [email, settings.EMAIL_HOST_USER]
				send_mail(email_subject, email_body,from_email,to_list, fail_silently=False)

			else:
				print signup.is_valid()   #form contains data and errors
        		print signup.errors

		elif 'login_submit' in request.POST:
			if login.is_valid():
				print "You are in login post"
				print request.POST
				email = login.cleaned_data['email']
				password = login.cleaned_data['password']
				print email,password
				user = authenticate(email=email, password=password)
				if user is not None:
					if user.is_active:	
						auth_login(request, user)
						print("User is valid, active and authenticated")
				else:
					print("User is not valid.")
	print request.user
	return render_to_response("index.html",context,context_instance=RequestContext(request))

def register_confirm(request, activation_key):
	print "You are in register_confirm"
	print activation_key
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    # if request.user.is_authenticated():
    #     HttpResponseRedirect('/home')
	try:
		user_activation = UserActivation.objects.get(activation_key__exact=activation_key)
	except:
		return HttpResponseNotFound('<center><h1>Error 404<br>Page not found</h1></center>')
	print user_activation
    #check if the activation key has expired, if it hase then render confirm_expired.html
    # if user_activation.key_expires < timezone.now():
    #     return render_to_response('user_profile/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
	user = MyUser.objects.get(email__exact=user_activation)
	user.is_vertified = True
	user.save()
	return render_to_response('activation_confirm.html')
