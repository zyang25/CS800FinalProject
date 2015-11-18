from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from models import PostBase

class PostForm(ModelForm):
    short_image = forms.ImageField(label='short_image')
    class Meta:
        model = PostBase
        exclude = ("user_id",)
        # fields = {'title','start_time','date_range','location','short_description','long_description','short_image','category_id','user_id'}

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
      
        