from django.contrib import admin
from .models import Course, Lecture, Section, LectureComment

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','course_type')
    search_fields = ('title',)
    list_filter = ('course_type',)
    list_per_page = 10

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course',)
    list_per_page = 20
    search_fields = ('title',)
    list_filter = ('course',)
    
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'lecture_type',)
    list_filter = ('lecture_type', 'course',)
    list_per_page = 50
    search_fields = ('title','section',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(LectureComment)