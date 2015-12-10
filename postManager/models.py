from django.db import models
# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from .helpers import * 
from accounts.models import MyUser
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class PostBase(models.Model):
    title = models.CharField(max_length=30, blank=True, default='')
    start_time = models.DateTimeField(null=True, blank=True,)
    create_date = models.DateTimeField(auto_now_add=True)
    date_range = models.CharField(max_length=30, blank=True, default='')
    is_expired = models.BooleanField(default=False)
    location = models.CharField(max_length=50, blank=True, default='')
    short_description = models.CharField(max_length=255, blank=True, default='')
    long_description = models.TextField(max_length=2048, blank=True, default='')
    short_image = models.ImageField(upload_to=RandomFileName('short_img'))
    user_id = models.ForeignKey('accounts.MyUser', null=True)
    category_id = models.ForeignKey('Category')
    def __unicode__(self):
        return u'%s %s' % (self.id, self.title)
    
class MoreImg(models.Model):
    postBase = models.ForeignKey('PostBase',null=False,default='',related_name='more_img')
    description = models.CharField(max_length=30, blank=True, default='')
    moreImgs = models.ImageField(upload_to=RandomFileName('more_img'))   
    def __unicode__(self):
        return self.description
    
class Category(models.Model):
    name = models.CharField(max_length=63)
    is_active = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

class MessageBoard(models.Model):
    post_id = models.ForeignKey('PostBase',null=True)
    user_id = models.ForeignKey('accounts.MyUser',null=True)
    message = models.CharField(max_length=63)
    is_active = models.BooleanField(default=True)
    def __unicode__(self):
        return u'%s' % (self.id)
    
class Meta:
    app_label = "postManager"