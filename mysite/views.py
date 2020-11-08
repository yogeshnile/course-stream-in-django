from django.shortcuts import render, redirect
from .models import Course, Lecture, Section, LectureComment
from student.models import CourseSubscription, StudentInfo, PaymentProcess
from django.http import HttpResponseRedirect
import razorpay
import json

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
    if not Course.objects.filter(course_slug=slug).exists():
        return render(request, '404.html')
    else:
        course = Course.objects.filter(course_slug=slug).first()
        section = Section.objects.filter(course=course)
        lecture = Lecture.objects.filter(course=course)
        if request.user.is_authenticated == True:
            subscription_course = CourseSubscription.objects.filter(student=StudentInfo.objects.filter(username=request.user).first(), 
            course=course).first()
        else:
            subscription_course = None
        context = {
            "course":course,
            "section":section,
            "lecture":lecture,
            "subscription_course":subscription_course,
        }
        return render(request, 'course/course_detail.html', context)

def lecture_detail(request, slug, lecture_slug):
    if not Course.objects.filter(course_slug=slug).exists() or not Lecture.objects.filter(lecture_slug=lecture_slug).exists():
        return render(request, '404.html')
    else:
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

def Checkout(request, slug):
    if not Course.objects.filter(course_slug = slug).exists():
        return render(request, '404.html')
    else:
        if request.user.is_authenticated == True:
            course = Course.objects.filter(course_slug = slug).first()
            if course.course_price == 0:
                context = {
                    "course":course,
                }
            else:
                with open("secret key.json",'r') as secret:
                    key = json.load(secret)['razorpay']
                student = StudentInfo.objects.filter(username=request.user).first()
                client = razorpay.Client(auth=(key['key id'],key['key secret']))
                payment_id = client.order.create({'amount':course.course_price*100, 'currency':'INR','payment_capture':'1'})
                new_payment = PaymentProcess(student=student, course=course, order_id=payment_id['id'])
                new_payment.save()
                context = {
                    "course":course,
                    "payment":payment_id,
                    "student":student,
                    "key":key['key id'],
                }
            return render(request, 'course/checkout.html', context)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))