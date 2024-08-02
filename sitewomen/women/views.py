from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Страница приложения women</h1>')


def categories_by_id(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(
        f'<h1>Статьи по категориям</h1><p>cat_id: {cat_id}</p>'
        )


def categories_by_slug(request: HttpRequest, cat_slug: str) -> HttpResponse:
    return HttpResponse(
        f'<h1>Статьи по категориям</h1><p>cat_slug: {cat_slug}</p>'
        )


def archive(request: HttpRequest, year: int):
    if year > 2024:
        raise Http404()
    return HttpResponse(
        f'<h1>Архивные статьи</h1><p>Архив {year} года'
        )


def page_not_found(request: HttpRequest, exception: Exception) -> HttpResponse:
    return HttpResponse('<h1>Page not found</h1>')