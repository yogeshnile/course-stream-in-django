from django.shortcuts import render, redirect
from .models import Course, Lecture, Section, LectureComment
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'course/index.html')

def courses(request):
    course = Course.objects.all()
    context = {
        "course": course
    }
    return render(request, 'course/courses.html', context)

def course_detail(request, slug):
    course = Course.objects.filter(course_slug=slug).first()
    section = Section.objects.filter(course=course)
    lecture = Lecture.objects.filter(course=course)
    context = {
        "course":course,
        "section":section,
        "lecture":lecture
    }
    return render(request, 'course/course_detail.html', context)

def lecture_detail(request, slug, lecture_slug):
    course = Course.objects.filter(course_slug=slug).first()
    section = Section.objects.filter(course=course)
    lecture = Lecture.objects.filter(course=course)
    video = Lecture.objects.filter(lecture_slug=lecture_slug).first()
    Lecture_Comment = LectureComment.objects.filter(lecture=video)

    context ={
        "course":course,
        "section":section,
        "lecture":lecture,
        "video":video,
        "lecture_comment":Lecture_Comment,
    }
    return render(request, 'course/lecture.html', context)

def pricing(request):
    course = Course.objects.filter(course_type="PAID")
    context = {
        "course": course
    }
    return render(request, 'course/pricing.html', context)

def videoComment(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            comment = request.POST['comment']
            lecture_id = request.POST['lecture_id']
            video = Lecture.objects.filter(id= lecture_id).first()
            new_comment = LectureComment(comment=comment, user=request.user, lecture=video)
            new_comment.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('home')