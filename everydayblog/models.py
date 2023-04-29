from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS_CHOICES = (('d', 'Draft'), ('p', 'Published'), ('r', 'Public request'), ('o', 'Public'))  # 'd' and 'p' is for user in blog, 'r' is for user if they whant it to be public. 'o' for admin to decide to be plublic.

class Post(models.Model):    # Django db queries
    title = models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='everydayblog_post')
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
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
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
# Create your models here.
