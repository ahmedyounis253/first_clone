from django.db import models
from django.db.models.base import ModelState
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=200)
    text=models.TextField()
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    create_time=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:postlist')

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text=models.TextField()
    create_time=models.DateTimeField(default=timezone.now)
    approve_comment=models.BooleanField(default=False)
    def approve(self):
        self.approve_comment=True
        self.save()
    def __str__(self):
        return self.text
    def get_absolute_url(self):
        return reverse('post_list')

