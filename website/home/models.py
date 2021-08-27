from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import slugify
from django.contrib.auth import settings
from ckeditor_uploader.fields import RichTextUploadingField
from .utils import *
from PIL import Image


class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, editable=False)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self):
        self.slug = slugify(self.name)
        return super().save()

    def __str__(self):
        """Unicode representation of Category."""
        return f"{self.name}"


def upload_location(instance, filename):
    return f'image/artikel/{instance.id}/{filename}'


def thumbnail(instance):
    image_600 = (600, 600)
    image_500 = (500, 500)
    pat = instance.image.path.split("\\")
    upat = '/'.join(pat[:-1])
    ur = instance.image.url.split('/')
    imag = ur[-1]
    img = Image.open(instance.image.path)
    img.thumbnail(image_600)
    instance.image = f'image/artikel/{instance.id}/600_{imag}'
    img.save(f'{upat}/600_{imag}')

    # img.thumbnail(image_600)
    # instance.thumbnail = f'image/artikel/{instance.id}/thumbnail600_{imag}'
    # img.save(f'{upat}/thumbnail600_{imag}')


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    judul = models.CharField(max_length=100, blank=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    isi = RichTextUploadingField()
    likes = models.ManyToManyField(User, related_name='likes_blog', blank=True)
    created = models.DateField(auto_now_add=True, blank=True, editable=False)
    updated = models.DateField(auto_now=True, blank=True, editable=False)
    published = models.BooleanField(default=False)
    snippet = models.TextField(blank=True)
    slug = models.CharField(max_length=100, blank=True, editable=False)
    shortcode = models.CharField(
        max_length=5, blank=True)

    def save(self):
        self.slug = slugify(self.judul)
        if not self.shortcode or self.shortcode == '':
            self.shortcode = check_code(self)
        super().save()
        if not '600' in self.image.name:
            thumbnail(self)
        return super().save()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id, 'judul': self.slug, 'category': slugify(self.category.first())})

    @property
    def num_likes(self):
        return self.likes.all().count()

    def __str__(self):
        return f'{self.judul} oleh {self.author}'


class Comment(models.Model):
    """Model definition for Comment."""

    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='article_comments')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    isi = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True, blank=True, editable=False)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        return f"{self.author}"
