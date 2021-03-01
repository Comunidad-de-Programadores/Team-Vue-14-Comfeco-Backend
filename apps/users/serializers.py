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
    password = serializers.CharField(write_only=True, required=True)
    
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
    birth_day = serializers.DateField(format="%d/%m/%Y", input_formats=["%d/%m/%Y", 'iso-8601'])

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'gender', 'birth_day',
            'country', 'facebook', 'github', 'twitter', 'linkedin', 'biography']


    def validate_username(self, value):
        request = self.context.get('request')
        user = request.user
        if User.objects.filter(username=value).exclude(id=user.id).exists():
            return serializers.ValidationError('Ya existe este username')
        return value
    
    def validate_email(self, value):
        request = self.context.get('request')
        user = request.user
        if User.objects.filter(email=value).exclude(id=user.id).exists():
            return serializers.ValidationError('Ya existe este email')
        return value


class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Los password no coinciden"})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "El password es incorrecto"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance