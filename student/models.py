from django.db import models
from django.contrib.auth.models import User
from mysite.models import Course
from django.utils.timezone import now

# Create your models here.
class StudentInfo(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12)
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.username.email} - {self.mobile_no}"

class CourseSubscription(models.Model):
    student = models.OneToOneField("student.StudentInfo", verbose_name=("username"), on_delete=models.CASCADE)
    course = models.OneToOneField("mysite.Course", verbose_name=("title"), on_delete=models.CASCADE)
    DateStamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.student.username} ==== {self.course}"