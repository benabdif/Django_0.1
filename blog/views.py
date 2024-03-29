from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Post

# This code to connecting with html page




def home(request):
    context = {
        'posts': Post.objects.all()
        #'posts': posts  This code to make data come for the tope
    }
    return render(request, 'blog/home.html', context)



class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailViem(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)   
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteViem(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
