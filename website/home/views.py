from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.


class ArticleListView(ListView):
    queryset = Article.objects.all().order_by('-updated')[:20]
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
            category__slug=self.kwargs['slug'])[:2]
        return queryset

    def get_context_data(self, **kwargs):
        self.extra_context['slug'] = self.kwargs['slug']
        self.kwargs.update(self.extra_context)
        return super().get_context_data()


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
