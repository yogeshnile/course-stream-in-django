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
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    DateStamp = models.DateTimeField(default=now)
    progress = models.CharField(default="0 %", max_length=10)
    payment_id = models.CharField(max_length=50, default="-")
    # order_id = 
    # razorpay_signature = 

    def __str__(self):
        return f"{self.student.username} ==== {self.course}"

# class PaymentProcess(models.Model):
    