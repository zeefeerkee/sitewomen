from django import template
from women.models import Category, TagArticle
from women import views

from django.db.models import Count

register = template.Library()


@register.inclusion_tag("women/list_categories.html")
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count("articles")).filter(total__gt=0)
    return {
        "cats": cats,
        "cat_selected": cat_selected,
    }


@register.inclusion_tag("women/list_tags.html")
def show_tags():
    cats = Category.objects.all()
    return {
        "tags": TagArticle.objects.annotate(total=Count("tags")).filter(total__gt=0),
    }
