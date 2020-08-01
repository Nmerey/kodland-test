from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm

class PostList(generic.ListView):
    queryset 		= Post.objects.order_by('-created_on')[:10]
    template_name 	= 'index.html'

class PostDetail(generic.DetailView):
    model 			= Post
    template_name 	= 'post_detail.html'

class PostCreate(generic.CreateView):
	model 			= Post
	form_class 		= PostForm
	template_name 	= 'post_form.html'
	success_url 	= '/'