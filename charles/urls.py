"""charles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from web.views import index
from checkout.views import checkout

# Rest
from rest_framework import routers, serializers, viewsets
from accounts.models import MyUser

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # Page
    url(r'^$', index, name='index'),
    url(r'^indextest/$', 'web.views.index_test', name='index_test'),
    # Account
    url(r'^user/$', 'accounts.views.account_admin',name="account_admin"),
    url(r'^user/profile$', 'accounts.views.user_profile',name="user_profile"),
    url(r'^user/activity/host$', 'accounts.views.user_activity_host',name="user_activity_host"),
    url(r'^user/activity/join$', 'accounts.views.user_activity_join',name="user_activity_join"),
    url(r'^user/activity/favorite$', 'accounts.views.user_activity_favorite',name="user_activity_favorite"),
    #url(r'^profile/$', 'accounts.views.account_profile',name="account_profile"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',name="user_logout"),
    url(r'^accounts/confirm/(?P<activation_key>\w+)/$', 'accounts.views.register_confirm',name="confirm_activation"),
    # Post
    url(r'^', include('postManager.urls')),
    # Auth
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # Api
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Checkout
    url(r'^activity/(?P<activity_id>[0-9]+)/$', 'checkout.views.checkout',name="activity_detail"),

]
