from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *

# Register your models here.
class CheckoutAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","post_id"]
	class Meta:
		model = Ticket

admin.site.register(Ticket,CheckoutAdmin)


class PurchaseDetailsAdmin(admin.ModelAdmin):
	list_display = ["__unicode__"]
	class Meta:
		model = PurchaseDetails

admin.site.register(PurchaseDetails,PurchaseDetailsAdmin)
