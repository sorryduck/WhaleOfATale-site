from django.db import models
from django.urls import reverse


class ArticleCommentaries(models.Model):
    username = models.CharField(max_length=100, blank=False)
    text = models.TextField(max_length=500, blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('Article', on_delete=models.PROTECT)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Commentary'
        verbose_name_plural = 'Commentaries'
        ordering = ['-id', 'username']


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-id', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-id', 'name']

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='news/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['time_create', 'title']


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'
