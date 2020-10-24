from django.contrib import admin
from .models import Post, BlogComment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author',)
    list_per_page = 20
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment)