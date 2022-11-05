from django.shortcuts import render
from .models import *
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .filters import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# def index(request):
#     post = Post.objects.all()
#     return render(request, 'index.html', context={'post': post})
#
#
# def detail(request, title):
#     info = Post.objects.get(title__iexact=title)
#     return render(request, 'info.html', context={'info': info})


class PostList(ListView):
    model = Post
    template_name = 'news/index.html'
    context_object_name = 'post'
    paginate_by = 2  # указываем количество записей на странице


class ShowPost(DetailView):
    model = Post
    template_name = 'news/info.html'
    # pk_url_kwarg: str = "pk"
    context_object_name = 'info'


class SearchPost(ListView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'search'
    paginate_by = 2  # указываем количество записей на странице

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# def create_post(request):
#     if request.method =='POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/news/')
#
#     form = PostForm
#     return render(request, 'create.html', {'form': form})


class CreatePost(CreateView):
    model = Post
    template_name = 'news/create.html'
    form_class = PostForm


class UpdatePost(UpdateView):
    model = Post
    template_name = 'news/create.html'
    form_class = PostForm


class DeletePost(DeleteView):
    model = Post
    template_name = 'news/delete.html'
    success_url = reverse_lazy('post_list')
    context_object_name = 'del_post'
