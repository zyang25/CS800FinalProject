from django.conf.urls import url
from postManager import api

urlpatterns = [
    url(r'^api/postlist/$', api.PostList.as_view()),
]