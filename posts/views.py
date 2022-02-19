from pyexpat import model
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class PostListView(ListView):
    template_name = "blog_post_list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "blog_post_detail.html"
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "new_blog_post.html"
    model = Post
    fields = ["title", "body", "author"]

class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    template_name = "edit_blog_post.html"
    model = Post
    fields = ["title", "body", "author"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeletView(LoginRequiredMixin , UserPassesTestMixin,DeleteView):
    template_name = "delete_blog_post.html"
    model = Post
    success_url = reverse_lazy('blog_post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user