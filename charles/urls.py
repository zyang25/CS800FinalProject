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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # Page
    url(r'^$', index, name='index'),
    url(r'^indextest/$', 'web.views.index_test', name='index_test'),
    # Account
    url(r'^user/$', 'accounts.views.account_admin',name="account_admin"),
    url(r'^user/profile$', 'accounts.views.account_profile',name="account_profile"),
    url(r'^profile/$', 'accounts.views.account_profile',name="account_profile"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',name="account_logout"),
    url(r'^accounts/confirm/(?P<activation_key>\w+)/$', 'accounts.views.register_confirm',name="confirm_activation"),
    # Post
    url(r'^', include('postManager.urls')),
    # Auth
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^checkout/$', 'checkout.views.checkout',name="checkout"),

]
