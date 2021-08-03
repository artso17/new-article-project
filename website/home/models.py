from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import slugify
from django.contrib.auth import settings
from ckeditor_uploader.fields import RichTextUploadingField
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


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    judul = models.CharField(max_length=100, blank=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='image/artikel',)
    isi = RichTextUploadingField()
    likes = models.ManyToManyField(User, related_name='likes_blog', blank=True)
    created = models.DateField(auto_now_add=True, blank=True, editable=False)
    updated = models.DateField(auto_now=True, blank=True, editable=False)
    published = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        super().save()
        self.slug = slugify(self.judul)
        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path, optimize=True, quality=30)
        return super().save()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id, 'slug': slugify(self.category.first())})

    @property
    def num_likes(self):
        return self.likes.all().count()

    def __str__(self):
        return f'{self.judul} oleh {self.author}'


class Comment(models.Model):
    """Model definition for Comment."""

    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    isi = models.TextField()

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        return f"{self.author}"
