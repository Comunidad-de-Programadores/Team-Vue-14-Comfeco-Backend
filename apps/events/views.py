from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from apps.core.permissions import AuthenticatedJWT
from .serializers import EventSerializer
from .models import Event


class EventAPI(AuthenticatedJWT, ListAPIView):
    model = Event
    queryset = Event.objects.all().order_by('-event_date')
    serializer_class = EventSerializer