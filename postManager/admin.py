from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","is_active"]
    class Meta:
        model = Category

class PostBaseAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","start_time","short_description","user_id","category_id"]
    class Meta:
        model = PostBase
    
class MoreImgAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    class Meta:
        model = MoreImg

admin.site.register(Category,CategoryAdmin)
admin.site.register(PostBase,PostBaseAdmin)
admin.site.register(MoreImg,MoreImgAdmin)