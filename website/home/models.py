from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    isi = RichTextUploadingField()

    def __str__(self):
        return f'{self.author}'
