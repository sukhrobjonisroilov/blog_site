from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    active = models.BooleanField(default=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email =models.EmailField(max_length=200)
    photos = models.ImageField(blank=True)


    def __str__(self):
        return f'{self.last_name}-{self.first_name}'

