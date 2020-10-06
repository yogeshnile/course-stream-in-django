from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
def info(request):
    return render(request, "student/info.html")

def ChangePassword(request):
    if request.method == 'POST':
        newpassword = request.POST['newPassword']
        users = User.objects.filter(username=request.user).first()
        users.set_password(newpassword)
        users.save()
        logout(request)
        return redirect("home")
    return render(request, "student/change_password.html")