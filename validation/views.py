from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect

# Create your views here.
def Usernamevalidation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric characters'}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'username already exists try another one'}, status=409)

        return JsonResponse({'username_valid':True})


def Emailvalidation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['emailid']
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'email already exists try another one'}, status=409)

        return JsonResponse({'email_valid':True})

def LoginUsernamevalidation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['login_username']

        if not User.objects.filter(username=username).exists():
            return JsonResponse({'login_username_error':'This username does not avilable please ragister first.'}, status=400)
        return JsonResponse({'login_username_valid':True})
    
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['emailid']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        # messages.success(request, "Account Create Successfully")
        
        return redirect('home')
    return redirect('home')

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