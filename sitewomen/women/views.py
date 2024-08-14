from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

menu = [
        {'title': 'о сайте', 'url_name': 'about'},
        {'title': 'добавить статью', 'url_name': 'addpage'},
        {'title': 'обратная связь', 'url_name': 'contact'},
        {'title': 'авторизация', 'url_name': 'login'},
    ]

articles_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.

    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',

     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]

# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'articles_db': articles_db,
        'cat_selected': 0,
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

def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'articles_db': articles_db,
        'cat_selected': cat_id,
        }
    return render(request, 'women/index.html', data)

def page_not_found(request, exception: Exception):
    return HttpResponse('<h1>Page not found</h1>')
