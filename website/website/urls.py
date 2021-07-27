"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import *

urlpatterns = [
    path('search-admin/', search_article_view, name='adminSearch'),
    path('admin-list/', admin_list_view, name='adminList'),
    path('delete/<str:model>/<str:pk>',
         ArticleDeleteView.as_view(), name='delete'),
    path('update/<str:model>/<str:pk>',
         ArticleUpdateView.as_view(), name='update'),
    path('create/<str:model>', ArticleCreateView.as_view(), name='create'),
    path('search/', search_view, name='searchView'),
    path('detail/<str:pk>/<slug:slug>',
         ArticleDetailView.as_view(), name='detail'),
    path('category/<slug:slug>', ArticleCategoryListView.as_view(), name='category'),
    path('', ArticleListView.as_view(), name='list'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
