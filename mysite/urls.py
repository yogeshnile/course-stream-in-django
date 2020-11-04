from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('pricing', views.pricing, name='pricing'),
    path('Courses/<str:slug>', views.course_detail, name='course_detail'),
    path('Courses/checkout/<str:slug>', views.Checkout, name='Checkout'),
    path('Courses/<str:slug>/<str:lecture_slug>', views.lecture_detail, name='lecture_detail'),
    path('courses/lecture/comment', views.videoComment, name='videoComment'),
]
