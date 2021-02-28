from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class UserLoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        token['first_name'] = user.first_name

        return token

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, max_length=255, required=True,)
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    # username = serializers.CharField(
    #     required=True,
    #     max_length=255,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            return serializers.ValidationError('Ya existe este username')
        return value
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            return serializers.ValidationError('Ya existe este email')
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password': 'No coinciden las contraseñas'})
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'firt_name', 'last_name', 'username', 'email', 'gender', 'birth_day',
            'country', 'facebook', 'github', 'twitter', 'linkedin', 'biography']
