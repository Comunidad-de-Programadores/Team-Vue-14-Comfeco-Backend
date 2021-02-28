from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegisterSerializer, UserProfileSerializer, UserLoginSerializer
from apps.core.permissions import AuthenticatedJWT
from .models import User


class UserLoginAPI(TokenObtainPairView):
    serializer_class = UserLoginSerializer


class UserRegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserProfileAPI(AuthenticatedJWT, RetrieveUpdateAPIView):
    model = User
    serializer_class = UserProfileSerializer
    http_method_names = ['get', 'put', 'patch']

    def get_object():
        return self.request.user