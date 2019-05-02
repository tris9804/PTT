from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsSelf

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
