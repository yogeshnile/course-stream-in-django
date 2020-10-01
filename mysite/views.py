from django.shortcuts import render
from .models import Course, Lecture, Section

# Create your views here.
def home(request):
    return render(request, 'index.html')

def courses(request):
    course = Course.objects.all()
    context = {
        "course": course
    }
    return render(request, 'courses.html', context)

def course_detail(request, slug):
    course = Course.objects.filter(course_slug=slug).first()
    section = Section.objects.filter(course=course)
    lecture = Lecture.objects.filter(course=course)
    context = {
        "course":course,
        "section":section,
        "lecture":lecture
    }
    return render(request, 'course_detail.html', context)

def blog(request):
    return render(request, 'blog.html')

def pricing(request):
    return render(request, 'pricing.html')