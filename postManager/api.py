from .models import PostBase
from .models import MoreImg
from .models import Category
from .serializers import CategorySerializer
from .serializers import MoreImgSerializer
from .serializers import PostBaseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostList(APIView):
     def get(self, request, format=None):
        postList = PostBase.objects.all()
        serializer = PostBaseSerializer(postList,many=True)
        return Response(serializer.data)