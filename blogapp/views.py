from django.shortcuts import render
from .models import Category, BlogPost, Comment,User
from django.core.paginator import Paginator


# Create your views here.
def index_page(requests):
    blogs = BlogPost.objects.all()
    ctx = {
        'blogs': blogs

    }
    return render(requests, 'index.html', ctx)


def blog_post(requests, pk):
    post= BlogPost.objects.get(pk=pk)
    if requests.POST:
        comment = Comment()
        comment.name = requests.POST.get('name', "")
        comment.text = requests.POST.get('comment','')
        comment.post=post

        comment.save()
    comments = Comment.objects.filter(post=post)

    ctx = {
        'blogs': post,
        'comments': comments

    }
    return render(requests, 'blog-post.html', ctx)


def blog_list(requests):
    blogs = BlogPost.objects.all()
    page = Paginator(blogs, 3)
    page_number = requests.GET.get('page', 1)
    posts = page.get_page(page_number)
    ctx = {
        'blogs': blogs,
        'posts': posts

    }

    return render(requests, 'blog-list.html', ctx)


def paginations_page(requests):
    blogs = BlogPost.objects.all()
    page = Paginator(blogs, 3)
    page_number = requests.GET.get('page', 1)
    posts = page.get_page(page_number)
    ctx = {
        'blogs': blogs,
        'posts': posts

    }
    return render(requests, 'papka/pagination.html', ctx)


def about_page(requests):
    ctx = {

    }

    return render(requests, 'about.html', ctx)


def user_page(requests,pk):
    user = User.objects.get(pk=0)
    ctx = {
        'user':user
    }
    return render(requests,'user.html',ctx)
