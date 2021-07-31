from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy


def allowed_hosts(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user_group = None
            if request.user.groups.exists():
                user_group = request.user.groups.all()[0].name
                if user_group in allowed_groups:
                    return view_func(request, *args, **kwargs)
            return HttpResponseRedirect(reverse('list'))
        return wrapper_func
    return decorator
