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
    path('article/<int:article_id>/', views.show_article, name="article"),
    path('category/<int:cat_id>/', views.show_category, name="cat_by_id"),
]