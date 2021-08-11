from django_cleanup.signals import cleanup_pre_delete
import json
from .forms import *
from .models import *
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.db.models import Q
from django.contrib.auth.models import User, Group
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .decorators import allowed_hosts
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect


def show_more_comments_view(request):
    if request.is_ajax():
        pk = request.POST['pk']
        data = int(request.POST['data'])
        end_data = data+10
        curr_obj = Comment.objects.filter(article__id=pk)[data:end_data]
        qs = []
        for obj in curr_obj:
            item = {
                'author': obj.author.username,
                'isi': obj.isi,
            }
            qs.append(item)
        len_data = len(get_list_or_404(Comment, article__id=pk))
        print(len(get_list_or_404(Comment, article__id=pk)))
        return JsonResponse({'data': qs, 'end_data': end_data, 'len_data': len_data})
    return JsonResponse({})


@login_required
def comment_ajax_view(request):
    if request.is_ajax():
        pk = request.POST['pk']
        data = request.POST['data']
        Comment.objects.create(article=get_object_or_404(
            Article, id=pk), author=request.user, isi=data)
        curr_obj = Comment.objects.filter(article__id=pk).last()
        qs = [{
            'author': curr_obj.author.username,
            'isi': curr_obj.isi
        }]

    return JsonResponse({'data': qs})


@login_required
def likes_ajax_view(request):
    if request.is_ajax():
        pk = request.POST['data']

        obj = get_object_or_404(Article, id=pk)
        liked = False
        if request.user in obj.likes.all():
            obj.likes.remove(request.user)
        else:
            obj.likes.add(request.user)
            liked = True
        data = [{
            'num_likes': obj.num_likes,
            'liked': liked
        }]
        return JsonResponse({'data': data})


@login_required(login_url='account_login')
@allowed_hosts(allowed_groups=['superuser'])
def search_article_view(request):
    if request.is_ajax():
        res = None
        qs = []
        data = request.POST['data']
        if request.POST['nameInput'] == 'article_search':
            curr_objects = Article.objects.filter(
                Q(judul__icontains=data) | Q(category__name__icontains=data))
            if len(data) > 0:
                if len(curr_objects) > 0:
                    for obj in curr_objects:
                        item = {
                            'id': obj.id,
                            'judul': obj.judul,
                            'author': obj.author.first_name,
                            'updated': obj.updated.strftime('%d/%m/%y'),
                            'published': obj.published,
                            'category': [cate.name for cate in obj.category.all()],
                        }
                        qs.append(item)
                    return JsonResponse({'data': qs})
                else:
                    qs = 'oops... data tidak ditemukan.'
                    return JsonResponse({'data': qs})
            if len(data) == 0:
                qs = []
                for obj in Article.objects.all()[:30]:
                    item = {
                        'id': obj.id,
                        'judul': obj.judul,
                        'author': obj.author.first_name,
                        'updated': obj.updated.strftime('%d/%m/%y'),
                        'published': obj.published,
                        'category': [cate.name for cate in obj.category.all()],
                    }
                    qs.append(item)
                return JsonResponse({'data': qs})
        elif request.POST['nameInput'] == 'category_search':
            curr_objects = Category.objects.filter(
                Q(name__icontains=data))
            if len(data) > 0:
                if len(curr_objects) > 0:
                    for obj in curr_objects:
                        item = {
                            'id': obj.id,
                            'name': obj.name,
                        }
                        qs.append(item)
                    return JsonResponse({'data': qs})
                else:
                    qs = 'oops... data tidak ditemukan.'
                    return JsonResponse({'data': qs})
            if len(data) == 0:
                qs = []
                for obj in Category.objects.all()[:30]:
                    item = {
                        'id': obj.id,
                        'name': obj.name,
                    }
                    qs.append(item)
                return JsonResponse({'data': qs})
        elif request.POST['nameInput'] == 'user_search':
            curr_objects = User.objects.filter(
                Q(username__icontains=data) | Q(first_name__icontains=data) | Q(last_name__icontains=data))
            if len(data) > 0:
                if len(curr_objects) > 0:
                    for obj in curr_objects:
                        item = {
                            'id': obj.id,
                            'username': obj.username,
                            'is_active': obj.is_active,
                            'is_staff': obj.is_staff,
                            'is_superuser': obj.is_superuser,
                            'group': [group.name for group in obj.groups.all()],
                        }
                        qs.append(item)
                    return JsonResponse({'data': qs})
                else:
                    qs = 'oops... data tidak ditemukan.'
                    return JsonResponse({'data': qs})
            if len(data) == 0:
                qs = []
                for obj in User.objects.all()[:30]:
                    item = {
                        'id': obj.id,
                        'username': obj.username,
                        'is_active': obj.is_active,
                        'is_staff': obj.is_staff,
                        'is_superuser': obj.is_superuser,
                        'group': [group.name for group in obj.groups.all()],
                    }
                    qs.append(item)
                return JsonResponse({'data': qs})
        elif request.POST['nameInput'] == 'group_search':
            curr_objects = Group.objects.filter(
                Q(name__icontains=data))
            if len(data) > 0:
                if len(curr_objects) > 0:
                    for obj in curr_objects:
                        item = {
                            'id': obj.id,
                            'name': obj.name,
                        }
                        qs.append(item)
                        print(obj.id)
                    return JsonResponse({'data': qs})
                else:
                    qs = 'oops... data tidak ditemukan.'
                    return JsonResponse({'data': qs})
            if len(data) == 0:
                qs = []
                for obj in Group.objects.all()[:30]:
                    item = {
                        'id': obj.id,
                        'name': obj.name,
                    }
                    qs.append(item)
                return JsonResponse({'data': qs})
    return JsonResponse({})


@login_required(login_url='account_login')
@allowed_hosts(allowed_groups=['superuser'])
def admin_list_view(request):
    print(request.user.groups.all()[0])
    context = {
        'object_list': Article.objects.all(),
        'page_title': 'Admin List',
        'categories': Category.objects.all(),
        'users': User.objects.all().order_by('date_joined')[:20],
        'groups': Group.objects.all()[:20]
    }
    return render(request, 'admin_listview.html', context)


def search_view(request):
    context = {
        'page_title': 'pencarian',
        'categories': Category.objects.all(),
    }
    if request.method == 'POST' and request.POST['searched'] != ['']:
        search = request.POST['searched']
        article = Article.objects.filter(Q(judul__contains=search))
        if article.exists():
            context['object_list'] = article[:20]
    return render(request, 'article_list.html', context)


class GetQuerysetMixin:
    def get_queryset(self):
        if self.kwargs['model'] == 'article':
            queryset = Article.objects.all()
        elif self.kwargs['model'] == 'category':
            queryset = Category.objects.all()
        elif self.kwargs['model'] == 'user':
            queryset = User.objects.all()
        elif self.kwargs['model'] == 'group':
            queryset = Group.objects.all()
        return queryset


class GetFormClassMixin:
    def get_form_class(self):
        if self.kwargs['model'] == 'article':
            form_class = ArticleForm
        elif self.kwargs['model'] == 'category':
            form_class = CategoryForm
        elif self.kwargs['model'] == 'user':
            form_class = UserForm
        elif self.kwargs['model'] == 'group':
            form_class = GroupForm
        return form_class


class GetAbsoluteUrlMixin:
    def get_success_url(self):
        if self.kwargs['model'] == 'user' or self.kwargs['model'] == 'group' or self.kwargs['model'] == 'category':
            url = reverse('adminList')
        elif self.kwargs['model'] == 'article':
            url = self.object.get_absolute_url()
        return url


class ArticleListView(ListView):
    queryset = Article.objects.all().exclude(
        published=False).order_by('-updated')[:20]
    template_name = "article_list.html"
    extra_context = {'categories': Category.objects.all()}


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

    def get_context_data(self, **kwargs):
        self.extra_context = {
            'categories': Category.objects.all(),
            'curr_category': Category.objects.get(
                slug=self.kwargs['category']),
            'same_articles': Article.objects.filter(
                category__slug=self.kwargs['category']).exclude(Q(id=self.kwargs['pk']) | Q(published=False)).order_by('-updated')[:5],
            'comments': Comment.objects.filter(article__id=self.kwargs['pk'])[:10]
        }
        self.kwargs.update(self.extra_context)
        return super().get_context_data()


@ method_decorator(login_required, name='dispatch')
class ArticleDetailAuthView(ArticleDetailView):
    pass


@ method_decorator(allowed_hosts(allowed_groups=['superuser']), name='dispatch')
class ArticleCreateView(GetFormClassMixin, GetAbsoluteUrlMixin, CreateView):
    template_name = "article_edit.html"
    extra_context = {
        'page_title': 'Buat Blog'
    }


@ method_decorator(allowed_hosts(allowed_groups=['superuser']), name='dispatch')
class ArticleUpdateView(GetQuerysetMixin, GetFormClassMixin, GetAbsoluteUrlMixin, UpdateView):
    template_name = "article_edit.html"
    extra_context = {
        'page_title': 'Update Blog'
    }


@ method_decorator(allowed_hosts(allowed_groups=['superuser']), name='dispatch')
class ArticleDeleteView(GetQuerysetMixin, DeleteView):
    template_name = "delete_view.html"
    success_url = reverse_lazy('adminList')
