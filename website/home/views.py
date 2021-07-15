from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import *
# Create your views here.


class ArticleListView(ListView):
    queryset = Article.objects.all().exclude(
        published=False).order_by('-updated')[:20]
    template_name = "article_list.html"
    extra_context = {
        'page_title': 'list View',
        'categories': Category.objects.all(),
    }

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        return super().get_context_data()


class ArticleCategoryListView(ListView):
    template_name = "article_list.html"

    extra_context = {
        'page_title': 'list View',
        'categories': Category.objects.all()
    }

    def get_queryset(self):
        queryset = Article.objects.filter(
            category__slug=self.kwargs['slug']).exclude(published=False)[:20]
        return queryset

    def get_context_data(self, **kwargs):
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
        self.extra_context['category'] = Category.objects.get(
            slug=self.kwargs['slug'])
        self.extra_context['same_articles'] = Article.objects.filter(
            category__slug=self.kwargs['slug']).exclude(Q(id=self.kwargs['pk']) | Q(published=False)).order_by('-updated')[:5]
        self.kwargs.update(self.extra_context)
        print(self.extra_context['category'])
        return super().get_context_data()
