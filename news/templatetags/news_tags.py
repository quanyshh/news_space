from django import template
from news.models import Post, Comment
register = template.Library()


@register.simple_tag()
def coment_count(id):
    return Comment.objects.filter(post=id).count()
