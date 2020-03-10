from django.shortcuts import render
from blog.models import Post

def blog_list(request):
  posts = Post.objects.all()
  return render(request, 'blog/index.html', {'posts': posts})

def post(request, pk):
  post = Post.objects.get(pk=pk)
  return render(request, 'blog/post.html', {'post': post})