
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Exists, OuterRef
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post, Category
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 5


    def get_queryset(self):
    # Получаем обычный запрос
        queryset = super().get_queryset()
    # Используем наш класс фильтрации.
    # Сохраняем нашу фильтрацию в объекте класса,
    # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
    # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class PostListSearch(PostList):
    template_name = 'post_search.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('News_Portal.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        posts = form.save(commit=False)

        if self.request.path == "/article/create/":
            posts.categoryType = "AR"
        posts.save()
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = ('News_Portal.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    raise_exception = True
    permission_required = ('News_Portal.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class CategiryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.postCategory = get_object_or_404(Category, id = self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory = self.postCategory).order_by('-dateCreation')
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.postCategory.subscribers.all()
        context['postCategory'] = self.postCategory
        return context
