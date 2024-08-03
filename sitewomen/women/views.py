from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    data = {
        'title': 'О сайте',
        'menu': menu,
        }
    return render(request, 'women/index.html', data)

def about(request: HttpRequest):
    data = {
        'title': 'О сайте',
        'menu': menu,
        }
    return render(request, 'women/about.html', context=data)


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
        return redirect('cats_by_slug', 'music')
    return HttpResponse(
        f'<h1>Архивные статьи</h1><p>Архив {year} года'
        )


def page_not_found(request: HttpRequest, exception: Exception) -> HttpResponse:
    return HttpResponse('<h1>Page not found</h1>')