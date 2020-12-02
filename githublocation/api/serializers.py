from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'name', 'username', 'zipcode')


class UserGithubSerializer(serializers.ModelSerializer):
  name = serializers.CharField(read_only=True)
  class Meta:
    fields = ('name')
