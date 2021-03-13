from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.core.permissions import AuthenticatedJWT
from .models import User, UserEvent

from .serializers import (UserRegisterSerializer, UserProfileSerializer, UserLoginSerializer,
                            UserChangePasswordSerializer, UserChangePasswordSerializer, UserEventSerializer)


class UserLoginAPI(TokenObtainPairView):
    serializer_class = UserLoginSerializer


class UserRegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserProfileAPI(AuthenticatedJWT, RetrieveUpdateAPIView):
    model = User
    serializer_class = UserProfileSerializer
    http_method_names = ['get', 'put', 'patch']

    def get_object(self):
        return self.request.user


class UserChangePasswordAPI(AuthenticatedJWT, UpdateAPIView):
    model = User
    serializer_class = UserChangePasswordSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user


class UserEventAPI(AuthenticatedJWT, ListAPIView):
    serializer_class = UserEventSerializer
    queryset = UserEvent.objects.all()

    def get_queryset(self):
        queryset = UserEvent.objects.filter(user=self.request.user).select_related('event')
        return queryset