from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
    DetailView
)
from .models import PostView, Blog, Like, Comment
from .forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "list.html"


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "blog.html"

    def get_object(self, **kwargs):
        blog = super().get_object(**kwargs)
        PostView.objects.get_or_create(user=self.request.user, post=blog)
        return blog


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "update.html"
    success_url = "/"


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = "/"
    template_name = "delete.html"       


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "create.html"
    form_class = BlogForm
    success_url = "/"


def like_post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    qs = Like.objects.filter(user=request.user, post=post)
    if qs.exists():
        qs[0].delete()
    else:
        Like.objects.create(user=request.user, post=post)
    return redirect("/")
