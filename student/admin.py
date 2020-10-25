from django.contrib import admin
from .models import StudentInfo

# Register your models here.
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('username','mobile_no','dob','address')
    list_per_page = 20
    search_fields = ('username','mobile_no','address')

admin.site.register(StudentInfo, StudentInfoAdmin)