from django.shortcuts import render
from rest_framework import viewsets
from .models import Topic, Sort, Post, Option, Comment
from .serializers import TopicSerializer, SortSerializer, PostSerializer, PostSerializer, OptionSerializer, CommentSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class SortViewSet(viewsets.ModelViewSet):
    queryset = Sort.objects.all()
    serializer_class = SortSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer