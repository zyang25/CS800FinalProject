from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
class CheckoutAdmin(admin.ModelAdmin):
	list_display = ["__unicode__"]
	class Meta:
		model = Ticket

admin.site.register(Ticket,CheckoutAdmin)