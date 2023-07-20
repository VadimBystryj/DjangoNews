from django.contrib.auth.models import User
from .filters import PostFilter, C, F, X
from .forms import PostForm
from .models import Post, Comment, Category, Subscriptions
from django.urls import reverse

from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .filters import PostFilter
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Subscriptions, Category



class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_publication'] = "Чуть позже сообщим о предстоящих публикациях!"
        context['filterset'] = self.filterset
        return context

    def user_list(request):
        f = F(request.GET, queryset=User.objects.all())
        return render(request, 'user_t.html', {'filter': f})

    def posts_list(request):
        c = C(request.GET, queryset=Post.objects.all())
        return render(request, 'post_t.html', {'filter': c})

    def comment_list(request):
        x = X(request.GET, queryset=Comment.objects.all())
        return render(request, 'comment_t.html', {'filter': x})


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('News_Portal.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def create_post(request):
        form = PostForm()

        if request.method == 'POST':
            form = PostForm(request.POST)
            form.save()
            return HttpResponseRedirect('/posts/')
        form = PostForm()
        return render(request, 'post_create.html', {'form': form})


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = ('News_Portal.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    raise_exception = True
    permission_required = ('News_Portal.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'post_search'
    ordering = ['-time_of_creation']

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)

        if not self.request.GET:
            return queryset.none()

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.request = None

    def get_queryset(self):
        self.сategory = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.сategory).order_by('-dateCreation')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.сategory.subscribers.all()
        context['category'] = self.сategory
        return context


@login_required()
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'subscribe.html', {'category': category, 'message': message})


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscriptions.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscriptions.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscriptions.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )
