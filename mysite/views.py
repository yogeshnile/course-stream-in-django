from django.shortcuts import render, HttpResponse
from .models import Course

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
    return render(request, 'course_detail.html')

def blog(request):
    return render(request, 'blog.html')

def pricing(request):
    return render(request, 'pricing.html')