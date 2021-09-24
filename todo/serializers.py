from rest_framework import serializers
from .models import User, Task, SubTask


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['is_superuser', 'email', 'is_staff', 'id']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['name', 'is_complete', 'user', 'priority']
        fields = '__all__'


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'
