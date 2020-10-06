from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentInfo(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12)
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.username.email} - {self.mobile_no}"