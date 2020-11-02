from django.contrib import admin
from .models import StudentInfo, CourseSubscription

# Register your models here.
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('username','mobile_no','dob','address')
    list_per_page = 20
    search_fields = ('username','mobile_no','address')
    readonly_fields = ('username','mobile_no','dob','address')

class CourseSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('student','course','progress')
    list_per_page = 20
    search_fields = ('student','course')
    readonly_fields = ('DateStamp','progress')
    list_filter = ('student','course','DateStamp')

admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(CourseSubscription, CourseSubscriptionAdmin)