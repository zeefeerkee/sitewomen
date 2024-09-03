from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .models import Category, TagArticle, Women

menu = [
    {"title": "о сайте", "url_name": "about"},
    {"title": "добавить статью", "url_name": "addpage"},
    {"title": "обратная связь", "url_name": "contact"},
    {"title": "авторизация", "url_name": "login"},
]


# Create your views here.
def index(request):
    articles = Women.published.all().select_related("cat")
    data = {
        "title": "Главная страница",
        "menu": menu,
        "articles": articles,
        "cat_selected": 0,
    }
    return render(request, "women/index.html", data)


def about(request):
    data = {
        "title": "О сайте",
        "menu": menu,
    }
    return render(request, "women/about.html", context=data)


def show_article(request, article_slug: str):
    article = get_object_or_404(Women, slug=article_slug)

    data = {
        "title": article.title,
        "menu": menu,
        "article": article,
        "cat_selected": 1,
    }
    return render(request, "women/article.html", context=data)


def addpage(request):
    return HttpResponse("<h1>Добавление статьи</h1>")


def contact(request):
    return HttpResponse("<h1>Обратная связь</h1>")


def login(request):
    return HttpResponse("<h1>Авторизация</h1>")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    articles = Women.published.filter(cat_id=category.pk).select_related("cat")
    data = {
        "title": f"Рубрика {category.name}",
        "menu": menu,
        "articles": articles,
        "cat_selected": category.pk,
    }
    return render(request, "women/index.html", data)


def show_tag_articlelist(request, tag_slug):
    tag = get_object_or_404(TagArticle, slug=tag_slug)
    articles = tag.tags.filter(is_published=Women.Status.PUBLISHED)

    data = {
        "title": f"Тег: {tag.tag}",
        "menu": menu,
        "articles": articles,
        "cat_selected": None,
    }

    return render(request, "women/index.html", context=data)


def page_not_found(request, exception: Exception):
    return HttpResponse("<h1>Page not found</h1>")
