from rest_framework import serializers
from .models import Project, Task
from django.contrib.auth.models import User, Group, Permission


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
