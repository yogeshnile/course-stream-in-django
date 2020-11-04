from django.contrib import admin
from .models import Course, Lecture, Section, LectureComment

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','course_type','course_price')
    search_fields = ('title',)
    list_filter = ('course_type',)
    list_per_page = 10
    ordering = ['title']
    readonly_fields = ('course_slug',)
    # prepopulated_fields = {'course_slug':['title']}
    fieldsets = [
        ("UPDATE BY ADMIN", {'fields': ['title','description','thumbnail_url','course_type','course_length','course_price']}),
        ("UPDATE BY SYSTEM", {'fields': ['course_slug']}),
    ]

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
    readonly_fields = ('lecture_slug','course')
    fieldsets = [
        ("UPDATE BY ADMIN", {'fields': ['title','video_url','section','lecture_type']}),
        ("UPDATE BY SYSTEM", {'fields': ['course','lecture_slug']}),
    ]

class LectureCommentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('comment','user','lecture')
    list_filter = ('lecture',)
    search_fields = ('comment',)
    readonly_fields = ('timestamp',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(LectureComment, LectureCommentAdmin)