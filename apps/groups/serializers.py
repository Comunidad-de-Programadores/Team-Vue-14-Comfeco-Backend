from rest_framework import serializers
from apps.users.models import UserGroup
from .models import Group


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['name', 'image', 'description', 'tag', 'id']




class GroupRegisterSerializer(serializers.Serializer):

    group_id = serializers.IntegerField()
    
    def validate_group_id(self, value):
        user = self.context.get('request').user
        if not Group.objects.filter(id=value).exists():
            raise serializers.ValidationError('No existe un grupo')
        if UserGroup.objects.filter(group_id=value, user=user).exists():
            raise serializers.ValidationError('Ya se encuentra registrado')
        return value