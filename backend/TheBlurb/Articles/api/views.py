from django.contrib.auth.models import User
from .serializers import ArticleSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView 
from rest_framework.permissions import IsAdminUser

from Articles.models import Article

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

