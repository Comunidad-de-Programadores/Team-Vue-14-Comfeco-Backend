from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from apps.core.permissions import AuthenticatedJWT
from .serializers import EventSerializer, EventRegisterSerializer
from .models import Event
from apps.users.models import UserEvent


class EventAPI(AuthenticatedJWT, ListAPIView):
    model = Event
    queryset = Event.objects.all().order_by('-event_date')
    serializer_class = EventSerializer


class EventRegisterAPI(AuthenticatedJWT, APIView):

    def post(self, request, *args, **kwargs):
        serializer = EventRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event_id = serializer.data.get('event_id')
        UserEvent.objects.created(event_id=event_id, user=request.user)
        return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)