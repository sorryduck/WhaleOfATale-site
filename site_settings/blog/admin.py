from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content',)
    prepopulated_fields = {'slug': ('title',)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('id', 'name', 'email')


class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'username',)
    list_display_links = ('id', 'username',)
    search_fields = ('id', 'username', 'text')


admin.site.register(Article, ArticleAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(ArticleCommentaries, CommentaryAdmin)
