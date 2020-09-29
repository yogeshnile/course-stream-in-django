from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('blog', views.blog, name='blog'),
    path('pricing', views.pricing, name='pricing'),
    path('Courses/<str:slug>', views.course_detail, name='course_detail'),
]
