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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from home.views import *

urlpatterns = [
    path('delete-comment/', delete_comment, name='del_comment'),
    path("password-reset-confirm/<uidb64>/<token>", password_reset_user_confirm_view,
         name="password_reset_confirm"),
    path("password-reset-done/", PasswordResetUserDone.as_view(),
         name="password_reset_done"),
    path("password-reset/", PasswordResetUserView.as_view(), name="passwordReset"),
    path("activation/<uidb64>/<token>", activation_email_view, name="activate"),
    path("register/", create_user_view, name="register"),
    path('show-comment/', show_more_comments_view, name='showCommAjax'),
    path('add-comment/', comment_ajax_view, name='commentAjax'),
    path('likes/', likes_ajax_view, name='likesAjax'),
    path('search-admin/', search_article_view, name='adminSearch'),
    path('admin-list/', admin_list_view, name='adminList'),
    path('delete/<str:model>/<str:pk>',
         ArticleDeleteView.as_view(), name='delete'),
    path('update/<str:model>/<str:pk>',
         ArticleUpdateView.as_view(), name='update'),
    path('create/<str:model>', ArticleCreateView.as_view(), name='create'),
    path('search/', search_view, name='searchView'),
    path('detail/<slug:judul>/<str:pk>/<slug:category>',
         ArticleDetailView.as_view(), name='detail'),
    path('detail-auth/<slug:judul>/<str:pk>/<slug:category>',
         ArticleDetailAuthView.as_view(), name='detailAuth'),
    path('category/<slug:slug>', ArticleCategoryListView.as_view(), name='category'),
    path('', ArticleListView.as_view(), name='list'),
    path('admin/admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
