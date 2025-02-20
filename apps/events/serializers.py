from rest_framework import serializers
from apps.users.models import UserEvent
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['name', 'image', 'description', 'event_date', 'id']


class EventRegisterSerializer(serializers.Serializer):

    event_id = serializers.IntegerField()
    
    def validate_event_id(self, value):
        user = self.context.get('request').user
        if not Event.objects.filter(id=value).exists():
            raise serializers.ValidationError('No existe un evento')
        if UserEvent.objects.filter(event_id=value, user=user).exists():
            raise serializers.ValidationError('Ya se encuentra registrado')
        return value