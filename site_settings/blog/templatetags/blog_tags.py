from django import template

from ..forms import *

register = template.Library()


@register.inclusion_tag('blog/menu.html')
def menu_list():
    return {
        'categories': Category.objects.all()
    }


@register.inclusion_tag('blog/comments.html')
def comment_section(pk):

    return {
        'comments': ArticleCommentaries.objects.filter(article_id=pk),
    }
