from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

menu = [
        {'title': 'о сайте', 'url_name': 'about'},
        {'title': 'добавить статью', 'url_name': 'addpage'},
        {'title': 'обратная связь', 'url_name': 'contact'},
        {'title': 'авторизация', 'url_name': 'login'},
    ]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'data_db': data_db,
        }
    return render(request, 'women/index.html', data)

def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu,
        }
    return render(request, 'women/about.html', context=data)

def show_article(request, article_id: int):
    return HttpResponse(f"Отображение статьи с id = {article_id}")

def addpage(request):
    return HttpResponse('<h1>Добавление статьи</h1>')

def contact(request):
    return HttpResponse('<h1>Обратная связь</h1>')

def login(request):
    return HttpResponse('<h1>Авторизация</h1>')

def page_not_found(request, exception: Exception):
    return HttpResponse('<h1>Page not found</h1>')