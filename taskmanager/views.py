from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views import View
from django.contrib import messages

# adding models and their serializers
from .models import *
from django.contrib.auth.models import User, Group, Permission
from .serializers import *


# adding forms
from .forms import TrialForm, ProjectForm

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
# Create your views here.


class Home(View):

    def get(self, request, id=None):
        if id is not None:

            try:
                obj = Project.objects.get(pk=id)
                obj.status = "NOW TRACKING"
                obj.save()
                print("The Object status is now tracking")
                return HttpResponse(f"""
                <html>
                <body>
                Peoject Status Updated
                <a href="taskmanager:{obj.get_absolute_url}">{obj.name}</a>
                {TrialForm().as_p()}
                {ProjectForm().as_table()}
                </body>
                </html>
                """)
            except ObjectDoesNotExist:
                return HttpResponse("""<html>
                <body>
                The Object Does Not Exist
                </body>
                </html>
                """)
        pros = Project.objects.all()
        serialed = ProjectSerializer(pros, many=True)
        form = ProjectForm()
        return render(request, "base.html", context={"obj": "No Object passed", "form": form, "serialed": pros})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            print(form)
        else:
            print("No valid data")
        return redirect(DashboardView)


class ProjectAPIView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "pk"


class TaskAPIView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupAPIView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionAPIView(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class DashboardView(View):
    def get(self, request):
        pros = Project.objects.all()
        project = Project.objects.get(pk=1)
        projform = ProjectForm(instance=project)
        tasks = Task.objects.all()
        print(request.user)
        return render(request, 'dashboard.html', context={'form': projform,  "serialed": pros, 'obj': 'No Object Passed  here', 'tasks': tasks})

    def post(self, request):
        form = ProjectForm(request)
        if form.is_valid():
            print("The form was valid and all values passed")
            return reverse(home)


class CompleteTaskView(View):
    def post(self, request):
        id = request.POST["id"]
        print(id)
        obj = Task.objects.get(pk=id)
        print(obj)
        return reverse(home)


class ActiveTask(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'ongoing-tasks.html', context={'tasks': tasks})


class OngoingProjectView(View):
    def get(self, request, projid=None):
        if projid is None:
            return HttpResponseRedirect("/")
        messages.success(request, "The Object Loading was Successful")
        project = Project.objects.get(pk=projid)
        proj_tasks = Task.objects.filter(project=project)
        print(proj_tasks)
        return render(request, "mytask.html", context={'proj_tasks': proj_tasks})
