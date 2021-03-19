from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, DestroyAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from apps.core.permissions import AuthenticatedJWT
from .serializers import EventSerializer, EventRegisterSerializer
from .models import Event
from apps.users.models import UserEvent


class EventAPI(AuthenticatedJWT, ListAPIView):
    model = Event
    queryset = Event.objects.all().order_by('-event_date')
    serializer_class = EventSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'events': list(self.request.user.user_events.all().values_list('event_id', flat=True))
        }

        
class EventRegisterUserAPI(AuthenticatedJWT, APIView):
    @swagger_auto_schema(
        request_body=EventRegisterSerializer,
        operation_id='Create User Event',
        tags=['events']
    )
    def post(self, request, *args, **kwargs):
        serializer = EventRegisterSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        event_id = serializer.data.get('event_id')
        UserEvent.objects.create(event_id=event_id, user=request.user)
        return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
