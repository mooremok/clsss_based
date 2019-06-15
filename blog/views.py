from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . models import Post

class PostListView(ListView):

    model = Post
    paginate_by = 2 #20条记录分页
    template_name = 'blog/blog_list.html'
    context_object_name = 'post_list'    

class PostDetailVies(DetailView):
    
    model = Post
    template_name = 'blog/blog_detail.html'