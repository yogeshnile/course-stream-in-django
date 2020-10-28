from django.contrib import admin
from .models import Post, BlogComment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author',)
    list_per_page = 20
    search_fields = ('title',)
    readonly_fields = ('slug','timeStamp')

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('comment','post','user','timestamp')
    list_per_page = 20
    search_fields = ('comment',)
    list_filter = ('post',)
    readonly_fields = ('timestamp',)

admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)