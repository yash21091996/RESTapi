from django.contrib.auth.models import User, Group
from client.models import Client, Project
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         field = ('client_name')

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        field ='__all__'