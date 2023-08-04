from django.urls import path
from .views import index_page,blog_post,blog_list,about_page,user_page
urlpatterns = [
    path('',index_page,name='index_page'),
    path('blog_post/<int:pk>',blog_post,name = 'blog_post'),
    path('blog_list/',blog_list,name='blog_list'),
    path('about/',about_page,name='about'),



]