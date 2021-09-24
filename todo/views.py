from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import User, Task, SubTask
from .serializers import TaskSerializer, UserSerializer, SubTaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        tasks = Task.objects.all()
        if not request.user.is_staff:
            tasks = tasks.filter(user=request.user)  # only for current user
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        if task and (request.user.is_staff or task.user.id == request.user.id):
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, pk=None):
    #     task = Task.objects.get(pk=pk)
    #     serializer = TaskSerializer(task, data=request.data, partial=True)
    #     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        if task:
            task.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SubTaskViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        subTasks = SubTask.objects.all()
        if not request.user.is_staff:
            tasks = subTasks.filter(user=request.user)  # only for current user
        serializer = SubTaskSerializer(subTasks, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SubTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        sub_task = get_object_or_404(SubTask, pk=pk)
        if request.user.is_staff or sub_task.task.id == request.user.id:
            serializer = SubTaskSerializer(sub_task)
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        sub_task = get_object_or_404(SubTask, pk=pk)
        serializer = SubTaskSerializer(sub_task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, pk=None):
    #     task = SubTask.objects.get(pk=pk)
    #     serializer = SubTaskSerializer(task, data=request.data, partial=True)
    #     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        sub_task = get_object_or_404(SubTask, pk=pk)
        if sub_task:
            sub_task.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
