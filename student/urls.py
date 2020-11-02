from django.urls import path
from . import views

urlpatterns = [
    path('info', views.info, name="info"),
    path('change-password', views.ChangePassword, name="ChangePassword"),
    path('courses', views.UserCourse, name="UserCourse"),
]
