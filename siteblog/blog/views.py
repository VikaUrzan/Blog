from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator


class Home(ListView):
    model = Post
    template_name = 'blog/home_blog.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


def get_category(request, slug):
    return render(request, 'blog/category.html')


def get_post(request, slug):
    return render(request, 'blog/home_blog.html')

