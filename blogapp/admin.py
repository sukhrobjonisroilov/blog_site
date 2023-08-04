from django.contrib import admin
from .models import Category,BlogPost,Comment,User
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(User)
