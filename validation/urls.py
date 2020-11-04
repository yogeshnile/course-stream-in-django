from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('username', csrf_exempt(views.Usernamevalidation), name='Usernamevalidation'),
    path('email', csrf_exempt(views.Emailvalidation), name='Emailvalidation'),
    path('login-username', csrf_exempt(views.LoginUsernamevalidation), name='LoginUsernamevalidation'),
    path('password', csrf_exempt(views.currentPassvalidation), name='currentPassvalidation'),
    path('user/login', views.handlelogin, name='handlelogin'),
    path('user/logout', views.handlelogout, name='handlelogout'),
    path('user/signup', views.handleSignup, name='handleSignup'),
    path('course/check-payment/payment-ckecking', csrf_exempt(views.checkpayment), name='checkpayment'),
    path('Courses/check-payment/free/<str:slug>', views.FreeCheckout, name='FreeCheckout'),
]