from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from checkout.models import Ticket
from postManager.models import PostBase


# Create your views here.
@login_required(login_url='/')
def activity_detail(request,activity_id):
	template_name = 'activity_detail.html'
	postObject = PostBase.objects.get(pk=activity_id)
	
	tickets = Ticket.objects.filter(post_id = activity_id)
	context = {
	'tickets': tickets,
	'postObject' : postObject,
	}
	return render(request,template_name,context)