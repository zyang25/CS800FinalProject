from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from models import Ticket


class TicketForm(ModelForm):

	class Meta:
		model = Ticket
		fields = {'ticket_descrption','price'}
        exclude = ("post_id",)
