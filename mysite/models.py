from django.db import models
from django.utils.text import slugify

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

    def __str__(self):
        return f"{self.course_type} - {self.title}."

    def save(self, *args, **kwargs):
        self.course_slug = slugify(self.title)
        super().save(*args, **kwargs)

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.course}"