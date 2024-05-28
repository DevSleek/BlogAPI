from django.db import models
from users.models import User

from utils.models import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    is_published = models.BooleanField(default=False)
    is_recommend = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
