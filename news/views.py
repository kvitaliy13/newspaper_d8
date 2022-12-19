from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        authors_group.user_set.add(user)
    return redirect('/news')


class PostList(ListView):
      model = Post
      ordering = '-time_in_post'
      template_name = 'news.html'
      context_object_name = 'post'
      paginate_by = 10

      # Переопределяем функцию получения списка товаров
      def get_queryset(self):
          # Получаем обычный запрос
          queryset = super().get_queryset()
          self.filterset = PostFilter(self.request.GET, queryset)
          # Возвращаем из функции отфильтрованный список товаров
          return self.filterset.qs

      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          # Добавляем в контекст объект фильтрации.
          context['filterset'] = self.filterset
          return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post_id.html'
    context_object_name = 'post'

class SearchPosts(ListView):
    paginate_by = 10
    model = Post
    ordering = 'time_in_post'
    template_name = 'search.html'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_filter'] = self.filterset
        return context


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post',)

class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.change_post',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')
    permission_required = ('news.delete_post',)

class ArticleCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post',)

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = "Добавить статью"
        return context


class ArticleUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.change_post',)

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактировать статью"
        return context


class ArticleDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')
    permission_required = ('news.delete_post',)

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['title'] = "Удалить статью"
        context['previous_page_url'] = reverse_lazy('posts_list')
        return context




class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'
