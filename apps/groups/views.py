from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from apps.core.permissions import AuthenticatedJWT
from .serializers import GroupSerializer
from .models import Group


class GroupAPI(AuthenticatedJWT, ListAPIView):
    model = Group
    queryset = Group.objects.all().order_by('-created')
    serializer_class = GroupSerializer

    def get_queryset(self):
        language = self.request.query_params.get('language')
        search = self.request.query_params.get('search')
        queryset = Group.objects.all().order_by('-created')
        if language:
            queryset = queryset.filter(language=language)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset