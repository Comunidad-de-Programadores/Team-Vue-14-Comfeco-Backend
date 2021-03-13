from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['name', 'image', 'description', 'event_date', 'id']


class EventRegisterSerializer(serializers.Serializer):

    event_id = serializers.IntegerField()
    
    def validate_event_id(self, value):
        if not Event.objects.filter(id=value).exists():
            raise serializers.ValidationError('Event not register')
        return value