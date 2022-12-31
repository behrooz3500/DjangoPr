from django.db import models


class Category(models.Model):
    """A class to define different categories for posts"""
    name = models.CharField(max_length=99)

    def __str__(self):
        return self.name


class Post(models.Model):
    """A class to define posts in blog app"""
    title = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
