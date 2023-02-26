from django.db import models
from users.models import User
from django.db.models import SET_NULL
from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(
        upload_to='posts/images/miniatures', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title
