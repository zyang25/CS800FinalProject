from rest_framework import serializers

from .models import PostBase
from .models import Category
from .models import MoreImg

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'pk',
            'name',
            'is_active',
        )
        
        def __unicode__(self):
            return u"%i" % self.pk
        
        class Meta:
            verbose_name_plural = "Category"
            
class MoreImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreImg
        fields = (
            'pk',
            'postBase',
            'description',
            'moreImgs',
        )
        
        def __unicode__(self):
            return u"%i" % self.pk
        
        class Meta:
            verbose_name_plural = "MoreImg"



class PostBaseSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(source='id')
    more_img = MoreImgSerializer(many=True,required=False)
#    title = serializers.CharField(source='title')
#    start_time = serializers.DateTimeField(source='start_time')
#    create_date = serializers.DateTimeField(source='create_date')
#    date_range = serializers.CharField(source='date_range')
#    is_expired = serializers.BooleanField(source='is_expired')
#    location = serializers.CharField(source='location')
#    short_description = serializers.CharField(source='short_description')
#    long_description = serializers.TextField(source='long_description')
    class Meta:
        model = PostBase
        fields = (
            '_id',
            'title',
            'start_time',
            'create_date',
            'is_expired',
            'location',
            'short_description',
            'long_description',
            'short_image',
            'user_id',
            'more_img',
        )
        
        def __unicode__(self):
            return u"%i" % self.pk
        
        class Meta:
            verbose_name_plural = "PostBase"