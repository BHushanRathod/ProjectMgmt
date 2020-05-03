
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects, Task, SubTask
from .serializers import ProjectsSerializer, TaskSerializer, ProjectListSerializer, TaskSubTaskListSerializer
from django.contrib.auth.models import User as UserModel
from rest_framework.permissions import IsAuthenticated
from .utils import get_user


class ProjectDetailsList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, proj_id=None):
        user = get_user(request)
        if proj_id:
            if Projects.objects.filter(id=proj_id, is_active=True).exists():
                projobj = Projects.objects.get(id=proj_id)
                serializer = ProjectListSerializer(projobj, many=False)
                return Response({'success': True, 'desc': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'desc': 'Project Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            pro_obj = Projects.objects.filter(creator=UserModel.objects.get(id=user), is_active=True)
            serializer = ProjectsSerializer(pro_obj, many=True)
            print(serializer)
            return Response(serializer.data, template_name='index.html', status=status.HTTP_200_OK)

    def post(self, request):
        user = get_user(request)
        project = Projects.objects.create(
            title=request.data['title'],
            creator=UserModel.objects.get(id=user),
            assignee=UserModel.objects.get(id=request.data['assignee']),
            desc=request.data['desc'],
            duration=request.data['duration'],
            avatar=request.data['avatar']
        )
        project.save()
        return Response({'success': True, 'desc': 'Added'}, status=status.HTTP_201_CREATED)

    def put(self, request, proj_id=None):
        print("In ProjectDetails/put")
        user = get_user(request)
        if proj_id:
            if Projects.objects.filter(pk=proj_id, creator=user, is_active=True).exists():
                project = Projects.objects.get(pk=proj_id)
                project.title = request.data['title'],
                project.creator.id = user,
                proj_id.assignee = UserModel.objects.get(id=request.data['assignee'])
                project.desc = request.data['desc'],
                project.duration = request.data['duration'],
                project.avatar = request.data['avatar']
                project.save()
                return Response({'success': True, 'desc': 'Updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'desc': 'Project Not Found'}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'desc': 'Project ID not provided'}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, proj_id=None):
        user = get_user(request)
        if proj_id:
            if Projects.objects.filter(pk=proj_id, creator=user, is_active=True).exists():
                project = Projects.objects.get(pk=proj_id)
                project.is_active = False
                project.save()
                return Response({'success': True, 'desc': 'Deleted'}, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'desc': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'success': False, 'desc': 'Project ID Not Provided'}, status=status.HTTP_403_FORBIDDEN)


class TaskDetailsList(APIView):
    def get(self, request, task_id=None, proj_id=None):
        user = get_user(request)
        if proj_id:
            if Projects.objects.filter(id=proj_id, is_active=True).exists():
                projobj = Projects.objects.get(id=proj_id)
                if task_id:
                    if Task.objects.filter(id=task_id, is_active=True).exists():
                        taskobj = Task.objects.get(id=task_id)
                        if taskobj.project.id == projobj.id:
                            serializer = TaskSerializer(taskobj, many=False)
                            return Response({'success': True, 'desc': serializer.data}, status=status.HTTP_200_OK)
                        else:
                            return Response({'success': False, 'desc': 'Task Does not belogs to same project'},
                                            status=status.HTTP_403_FORBIDDEN)
                    else:
                        return Response({'success': False, 'desc': 'Task Not Found'}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'success': False, 'desc': 'Task ID not provided'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'success': False, 'desc': 'Project Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'success': False, 'desc': 'Project ID not provided'}, status=status.HTTP_403_FORBIDDEN)

    def post(self, request, proj_id=None):
        print("In post/TaskDetailsList")
        user = get_user(request)
        if proj_id:
            if Projects.objects.filter(id=proj_id, is_active=True).exists():
                projobj = Projects.objects.get(id=proj_id)
                task = Task.objects.create(
                    title=request.data['title'],
                    desc=request.data['desc'],
                    project=projobj,
                    status=request.data['status'],
                    creator_id=user,
                    assignee = UserModel.objects.get(id=request.data['assignee']),
                    completed_date=request.data['completed_date']
                )
                task.save()
                return Response({'success': True, 'desc': 'Task Added'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'success': False, 'desc': 'Project Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'success': False, 'desc': 'Project ID not provided'}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, proj_id=None, task_id=None):
        user = get_user(request)
        if proj_id:
            if Projects.objects.filter(id=proj_id, is_active=True).exists():
                projobj = Projects.objects.get(id=proj_id)
                if task_id:
                    if Task.objects.filter(id=task_id, is_active=True).exists():
                        taskobj = Task.objects.get(id=task_id)
                        taskobj.title = request.data['title']
                        taskobj.desc = request.data['desc']
                        taskobj.project = projobj
                        taskobj.status = request.data['status']
                        taskobj.creator_id = user
                        taskobj.planned_date = request.data['planned_date']
                        taskobj.accepted_date = request.data['accepted_date']
                        taskobj.completed_date = request.data['completed_date']
                        taskobj.save()
                        return Response({'success': True, 'desc': 'Task Updated'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'success': False, 'desc': 'Task Not Found'}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'success': False, 'desc': 'Task ID not provided'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'success': False, 'desc': 'Project Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'success': False, 'desc': 'Project ID not provided'}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, proj_id=None, task_id=None):
        user = get_user(request)
        if proj_id:
            if Projects.objects.filter(id=proj_id, is_active=True).exists():
                if task_id:
                    if Task.objects.filter(id=task_id, is_active=True).exists():
                        taskobj = Task.objects.get(id=task_id)
                        taskobj.is_active = False
                        return Response({'success': True, 'desc': 'Task Deleted'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'success': False, 'desc': 'Task Not Found'},
                                        status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'success': False, 'desc': 'Task ID not provided'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'success': False, 'desc': 'Project Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'success': False, 'desc': 'Project ID not provided'}, status=status.HTTP_403_FORBIDDEN)


class SubTaskDetails(APIView):

    def get(self, request, proj_id=None, task_id=None, subtask_id=None):
        if task_id:
            if Task.objects.filter(id=task_id, is_active=True).exists():
                taskobj = Task.objects.filter(id=task_id, is_active=True)
                serializer = TaskSubTaskListSerializer(taskobj, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, proj_id=None, task_id=None):
        user = get_user(request)
        if proj_id:
            if Projects.objects.filter(id=proj_id, is_active=True).exists():
                if task_id:
                    if Task.objects.filter(id=task_id, is_active=True).exists():
                        taskobj = Task.objects.get(id=task_id, is_active=True)
                        subtask = SubTask.objects.create(
                            subtitle=request.data['title'],
                            desc=request.data['desc'],
                            task=taskobj
                        )
                        subtask.save()
                        return Response({'success': True, 'desc': 'SubTask Added'}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({'success': False, 'desc': 'Task Not Found'}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'success': False, 'desc': 'Task ID not provided'}, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({'success': False, 'desc': 'Project Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'success': False, 'desc': 'Project ID not provided'}, status=status.HTTP_403_FORBIDDEN)

