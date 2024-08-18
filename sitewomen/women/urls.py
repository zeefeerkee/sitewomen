from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "4year")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name="addpage"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('article/<slug:article_slug>/', views.show_article, name="article"),
    path('category/<slug:cat_slug>/', views.show_category, name="category"),
    path('tag/<slug:tag_slug>/', views.show_tag_articlelist, name='tag'),
]