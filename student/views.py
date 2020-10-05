from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request, "student/info.html")