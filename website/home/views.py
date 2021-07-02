from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

    extra_context = {
        'page_title': 'list View'
    }

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        # kwargs = self.kwargs
        return super().get_context_data()
