from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/')
def activity_detail(request,activity_id):
	template_name = 'activity_detail.html'
	context = {}
	return render(request,template_name,context)