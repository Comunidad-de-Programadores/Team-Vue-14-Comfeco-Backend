from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterSerializer
from .models import User


class UserRegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer