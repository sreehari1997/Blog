from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(default="first-blog")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug':self.slug
        })
    
    def get_like_url(self):
        return reverse("like_post", kwargs={
            'slug':self.slug
        })
    
    @property
    def get_post_views(self):
        return self.postview_set.all().count()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    
    @property
    def get_like_count(self):
        return self.like_set.all().count()


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class PostView(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Like(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title