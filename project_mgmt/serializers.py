from rest_framework import serializers
from django.contrib.auth.models import User

from project_mgmt.models import Projects, Task, SubTask


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    TaskList = ProjectTaskSerializer(source='task_set', many=True, read_only=True)

    class Meta:
        model = Projects
        fields = ('id', 'title', 'desc', 'duration', 'avatar', 'is_active', 'TaskList')


class SubTaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'


class TaskSubTaskListSerializer(serializers.ModelSerializer):
    SubTaskList = SubTaskListSerializer(source='subtask_set', many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'project', 'status', 'creator', 'assignee', 'planned_date', 'SubTaskList')
