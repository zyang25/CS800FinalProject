from django.http import *
from django.shortcuts import render_to_response, RequestContext, render
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
#Forms
from .forms import SignUpForm, LoginForm
# Model
from accounts.models import MyUser,UserInfo, UserActivation
from postManager.models import PostBase
# Forms
from accounts.forms import UserProfile

# Create your views here.
def user_profile(request):
	
	if request.user.is_authenticated():
		
		userinfo = UserInfo.objects.get(owner=request.user.pk)
		
		context = {
		'user_info':userinfo,
		}

		if request.method == 'POST':
			userprofileform = UserProfile(request.POST or None)
			print userprofileform
			if userprofileform.is_valid():
				newprofile = userprofileform.save(commit=False)
				newprofile.owner = request.user
				newprofile.save()
				userinfo = UserInfo.objects.get(owner=request.user.pk)
				context = {
				'user_info':userinfo,
				}
				context.update(csrf(request))

		return render_to_response("account_profile.html",context,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/")

def register_confirm(request, activation_key):
	
	try:
		user_activation = UserActivation.objects.get(activation_key__exact=activation_key)
	except:
		return HttpResponseNotFound('<center><h1>Error 404<br>Page not found</h1></center>')
	
	# Get User instance
	user = MyUser.objects.get(email__exact=user_activation)
	user.is_vertified = True
	user.save()
	
	# Delete it
	user_activation.delete()
	return HttpResponse('<center><h1>Account activated<br></h1></center>')

@login_required(login_url='/')
def account_admin(request):
	template_name = 'user/user_admin.html'
	return render(request,template_name)

@login_required(login_url='/')
def user_profile(request):
	template_name = 'user/user_profile.html'

	userinfo = UserInfo.objects.get(owner=request.user.pk)
		
	context = {
	'user_info':userinfo,
	}

	if request.method == 'POST':
		userprofileform = UserProfile(request.POST or None)
		print userprofileform
		if userprofileform.is_valid():
			newprofile = userprofileform.save(commit=False)
			newprofile.owner = request.user
			newprofile.save()
			userinfo = UserInfo.objects.get(owner=request.user.pk)
			context = {
			'user_info':userinfo,
			}
			context.update(csrf(request))

	return render(request,template_name,context)

@login_required(login_url='/')
def user_activity_host(request):
	template_name = 'user/user_activity_host.html'
	post_object = PostBase.objects.filter(user_id=request.user)
	context = {'posts':post_object}
	return render(request,template_name,context)

@login_required(login_url='/')
def user_activity_join(request):
	template_name = 'user/user_activity_join.html'
	post_object = PostBase.objects.filter(user_id=request.user)
	context = {'posts':post_object}
	return render(request,template_name,context)

@login_required(login_url='/')
def user_activity_favorite(request):
	template_name = 'user/user_activity_favorite.html'
	context = {}
	return render(request,template_name,context)
