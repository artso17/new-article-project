from django.contrib import admin

# Register your models here.
from .models import *


class Readonly(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(Article)
admin.site.register(Category, Readonly)
admin.site.register(Comment)
