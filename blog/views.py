from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_courses(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_courses.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})