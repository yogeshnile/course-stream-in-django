from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from student.models import StudentInfo, CourseSubscription, PaymentProcess
from mysite.models import Course
from student.models import CourseSubscription, StudentInfo

# Create your views here.
def checkpayment(request):
    if request.method == "POST":
        payment_id = request.POST['razorpay_payment_id']
        order_id = request.POST['razorpay_order_id']
        razorpay_signature = request.POST['razorpay_signature']

        course_details = PaymentProcess.objects.filter(order_id=order_id).first()
        course_details.payment_status = True
        course_details.save()

        complete_payment = CourseSubscription(student=course_details.student, course=course_details.course,
        payment_id=payment_id, order_id=order_id)
        complete_payment.save()

        return redirect('UserCourse')
    return redirect('home')

def FreeCheckout(request, slug):
    course = Course.objects.filter(course_slug=slug).first()
    if course.course_type == "FREE":
        student = StudentInfo.objects.filter(username=request.user).first()
        new_sub = CourseSubscription(student=student, course=course, payment_id="FREE", order_id="FREE")
        new_sub.save()
        return redirect('UserCourse')
    else:
        return redirect('home')

def currentPassvalidation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        currentPass = data['password']
        users = User.objects.filter(username=request.user).first()
        valid = users.check_password(currentPass)
        if not valid:
            return JsonResponse({'password_error':'Your password is not correct.'})
        else:
            return JsonResponse({'password_valid':True})


def Usernamevalidation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric characters'})
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'username already exists try another one'})

        return JsonResponse({'username_valid':True})


def Emailvalidation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['emailid']
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'email already exists try another one'})

        return JsonResponse({'email_valid':True})

def LoginUsernamevalidation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['login_username']

        if not User.objects.filter(username=username).exists():
            return JsonResponse({'login_username_error':'This username does not avilable please ragister first.'}) # 'status=400' write when debug
        return JsonResponse({'login_username_valid':True})
    
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['emailid']
        password = request.POST['password']
        mobile = request.POST['mobileno']
        dob = request.POST['dob'] #output yyyy-mm-dd
        address = request.POST['address']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        myuser = User.objects.filter(username=username).first()
        student_detail = StudentInfo.objects.create(username=myuser, email_id=email, mobile_no=mobile, dob=dob, address=address)
        student_detail.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['login_username']
        loginpassword = request.POST['login_password']

        user = authenticate(username=username, password=loginpassword)
        if user is not None:
            auth_login(request,user)
            #messages.success(request, "Successfully Logged In")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            #messages.error(request, "Login Unsuccessful")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def handlelogout(request):
    logout(request)
    #messages.success(request, "Logout Successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))