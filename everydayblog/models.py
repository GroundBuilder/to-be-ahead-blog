from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = (('d', 'Draft'), ('p', 'Published'), ('r', 'Public request'), ('o', 'Public'))  # 'd' and 'p' is for user in blog, 'r' is for user if they whant it to be public. 'o' for admin to decide to be plublic.

class Post(models.Model):    # Django db queries
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    title = models.CharField(max_length=220, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='everydayblog_post')
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):     # Django db queries
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    name =  models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title



# Create your models here.
