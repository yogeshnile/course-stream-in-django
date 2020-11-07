from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.timezone import now
import string, random

def get_random_string(lenght):
    letter = string.ascii_letters
    return ''.join(random.choice(letter) for i in range(lenght))

# Create your models here.

COURSE_TYPE = [
    ("FREE","FREE"),
    ("PAID","PAID"),
]

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail_url = models.CharField(max_length=100)
    course_type = models.CharField(max_length=4,choices=COURSE_TYPE, default="FREE")
    course_length = models.CharField(max_length=20)
    course_slug = models.SlugField(default="-")
    course_price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.course_type} - {self.title}."

    def save(self, *args, **kwargs):
        self.course_slug = slugify(self.title)
        self.course_slug += f"-{get_random_string(10)}"
        if self.course_type == "FREE":
            course_price = 0
        super().save(*args, **kwargs)

class Section(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.course}"

LECTURE_TYPE = [
    ("PREMIUM","PREMIUM"),
    ("NOT PREMIUM","NOT PREMIUM"),
]

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True)
    lecture_slug = models.SlugField(default="-")
    lecture_type = models.CharField(max_length=12, choices=LECTURE_TYPE, default="PREMIUM")
    
    def save(self, *args, **kwargs):
        self.course = self.section.course
        self.lecture_slug = slugify(self.title)
        self.lecture_slug += f"-{get_random_string(10)}"
        if self.section.course.course_type == "FREE":
            self.lecture_type = "NOT PREMIUM"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.section} - {self.lecture_type}"

class LectureComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.id} - {self.user.username} - {self.comment[0:15]} ..."