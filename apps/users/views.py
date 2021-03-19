from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, ListAPIView, 
                                    RetrieveAPIView, DestroyAPIView)
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.core.permissions import AuthenticatedJWT
from .models import User, UserEvent, UserGroup

from .serializers import (UserRegisterSerializer, UserProfileSerializer, UserLoginSerializer,
                            UserChangePasswordSerializer, UserChangePasswordSerializer, UserEventSerializer, UserGroupSerializer, UserSerializer)


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


class UserGroupsAPI(AuthenticatedJWT, ListAPIView):
    serializer_class = UserGroupSerializer
    queryset = UserGroup.objects.all()

    def get_queryset(self):
        queryset = UserGroup.objects.filter(user=self.request.user).select_related('event')
        return queryset



class UserGroupsDetailAPI(AuthenticatedJWT, RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = User.objects.filter(user_groups__group_id=self.kwargs.get('pk')).exclude(id=self.request.id).prefetch_related('user_groups__group')
        return queryset


class UserGroupDeleteAPI(AuthenticatedJWT, DestroyAPIView):

    def get_object(self):
        return get_object_or_404(UserGroup.objects.filter(user=self.request.user), group_id=self.kwargs.get('pk'))

        
class UserEventDeleteAPI(AuthenticatedJWT, DestroyAPIView):

    def get_object(self):
        return get_object_or_404(UserEvent.objects.filter(user=self.request.user), group_id=self.kwargs.get('pk'))
