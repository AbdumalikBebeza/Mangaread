from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(min_length=4, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {"password": {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["token"]
