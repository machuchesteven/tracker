from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('project', ProjectAPIView, basename="project")
router.register('task', TaskAPIView, basename="task")
router.register('user', UserAPIView, basename="user")
router.register('group', GroupAPIView, basename="group")
router.register('permission', PermissionAPIView, basename="permission")


urlpatterns = [
    path('', Home.as_view(), name="Homepage"),
    path('<int:id>', Home.as_view()),
    path('', include(router.urls)),
    path('dashboard', DashboardView.as_view(), name="dashboard"),
    path('complete', CompleteTaskView.as_view(), name="complete"),
    path('active', ActiveTask.as_view(), name="active"),
    path('actproject/<int:projid>',
         OngoingProjectView.as_view(), name="ongoing_project"),
    path('actproject', OngoingProjectView.as_view(), name="ongoing_project"),

]
