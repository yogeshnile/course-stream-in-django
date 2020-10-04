from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    content = models.TextField()
    slug = models.SlugField(default="-")
    timeStamp = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.author} - {self.title}"

class BlogComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.id} - {self.user.username} - {self.comment[0:15]} ..."