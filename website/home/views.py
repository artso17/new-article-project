import json
from .forms import *
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.contrib.auth.models import User
from .models import *
# Create your views here.

from django.http import JsonResponse


def search_article_view(request):
    # print(request.is_ajax())
    if request.is_ajax():
        data = request.POST['data']
        print(data)
        return JsonResponse({'data': data})
    return JsonResponse({})
    # if request.method == 'POST':
    # print(request.POST.__contains__('category_search'))
    # print(request.POST == 'category_search')
    # if request.POST.__contains__('category_search'):
    #     print('true ini category search')
    # if request.POST.__contains__('article_search'):
    #     print('true ini article search')


def admin_list_view(request):
    context = {
        'object_list': Article.objects.all(),
        'page_title': 'Admin List',
        'categories': Category.objects.all(),
        'users': User.objects.all().order_by('date_joined')[:20]
    }
    return render(request, 'admin_listview.html', context)


def search_view(request):
    context = {
        'page_title': 'pencarian',
        'categories': Category.objects.all(),
    }
    if request.method == 'POST' and request.POST['searched'] != ['']:
        # print(request.POST)
        search = request.POST['searched']
        article = Article.objects.filter(Q(judul__contains=search))
        if article.exists():
            context['object_list'] = article[:20]
    return render(request, 'article_list.html', context)


class ArticleListView(ListView):
    queryset = Article.objects.all().exclude(
        published=False).order_by('-updated')[:20]
    template_name = "article_list.html"
    extra_context = {
        'categories': Category.objects.all(),
    }

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        return super().get_context_data()


class ArticleCategoryListView(ListView):
    template_name = "article_list.html"

    extra_context = {
        'categories': Category.objects.all(),
    }

    def get_queryset(self):
        queryset = Article.objects.filter(
            category__slug=self.kwargs['slug']).exclude(published=False)[:20]
        return queryset

    def get_context_data(self, **kwargs):
        self.extra_context['curr_page'] = Category.objects.get(
            slug=self.kwargs['slug']).name
        self.extra_context['slug'] = self.kwargs['slug']
        self.kwargs.update(self.extra_context)
        return super().get_context_data()


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    extra_context = {
        'categories': Category.objects.all()
    }

    def get_context_data(self, **kwargs):
        self.extra_context['curr_category'] = Category.objects.get(
            slug=self.kwargs['slug'])
        self.extra_context['same_articles'] = Article.objects.filter(
            category__slug=self.kwargs['slug']).exclude(Q(id=self.kwargs['pk']) | Q(published=False)).order_by('-updated')[:5]
        self.kwargs.update(self.extra_context)
        # print(self.extra_context['category'])
        return super().get_context_data()


# class AdminListView(ListView):
#     template_name = "admin_listview.html"
#     model = Article
#     extra_context = {
#         'page_title': 'Admin list',
#         'categories': Category.objects.all()[:20],
#         'users': User.objects.all().order_by('date_joined')[:20],
#     }


class ArticleCreateView(CreateView):
    template_name = "article_edit.html"
    extra_context = {
        'page_title': 'Buat Blog'
    }

    def get_form_class(self):
        if self.kwargs['model'] == 'article':
            form_class = ArticleForm
        if self.kwargs['model'] == 'category':
            form_class = CategoryForm
        if self.kwargs['model'] == 'user':
            form_class = UserForm
        if self.kwargs['model'] == 'group':
            form_class = GroupForm
        return form_class

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        return super().get_context_data()
