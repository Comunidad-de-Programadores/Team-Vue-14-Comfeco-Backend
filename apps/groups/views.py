from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from apps.core.permissions import AuthenticatedJWT
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from apps.users.models import UserGroup
from .serializers import GroupSerializer, GroupRegisterSerializer
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

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'groups': self.request.user.user_groups.all().values_list('group_id', flat=True)
        }
        
class GroupRegisterUserAPI(AuthenticatedJWT, APIView):
    @swagger_auto_schema(
        request_body=GroupRegisterSerializer,
        operation_id='Create User Group',
        tags=['groups']
    )
    def post(self, request, *args, **kwargs):
        serializer = GroupRegisterSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        group_id = serializer.data.get('group_id')
        UserGroup.objects.created(group_id=group_id, user=request.user)
        return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)