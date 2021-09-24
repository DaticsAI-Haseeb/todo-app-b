from rest_framework import serializers
from .models import User, Task, SubTask


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['is_superuser', 'email', 'is_staff', 'id']


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'name', 'date_created', 'last_update', 'is_complete']


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'date_created', 'last_update', 'is_complete', 'user', 'priority', 'subtasks']

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks')
        task = Task.objects.create(**validated_data)
        for subtask_data in subtasks_data:
            SubTask.objects.create(task=task, **subtask_data)
        return task
