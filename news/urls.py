from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, SearchPosts, ArticleDelete, ArticleUpdate, ArticleCreate
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView
from .views import upgrade_me


urlpatterns = [
   path('', PostList.as_view(), name='news_list'),
   path('<int:pk>', PostDetail.as_view(), name='news_detail'),
   path('create/', PostCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
   path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('login/', LoginView.as_view(template_name='login.html'),name='login'),
   path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'),
   path('signup/',BaseRegisterView.as_view(template_name='signup.html'),name='signup'),
   path('upgrade/', upgrade_me, name = 'upgrade')
]

