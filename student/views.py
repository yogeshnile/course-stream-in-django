from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import CourseSubscription, StudentInfo

# Create your views here.
def info(request):
    if request.user.is_authenticated == True:
        return render(request, "student/info.html")
    return redirect("home")

    
def ChangePassword(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            newpassword = request.POST['newPassword']
            users = User.objects.filter(username=request.user).first()
            users.set_password(newpassword)
            users.save()
            logout(request)
            return redirect("home")
        return render(request, "student/change_password.html")
    return redirect("home")

def UserCourse(request):
    if request.user.is_authenticated == True:
        user = StudentInfo.objects.filter(username=request.user).first()
        ucourse = CourseSubscription.objects.filter(student=user)
        contest = {
            "ucourse":ucourse,
        }
        return render(request, "student/user_course.html", contest)
    return redirect("home")