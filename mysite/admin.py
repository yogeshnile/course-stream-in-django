from django.contrib import admin
from .models import Course, Lecture, Section, LectureComment

# Register your models here.
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lecture)
admin.site.register(LectureComment)