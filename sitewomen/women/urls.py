from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "4year")

urlpatterns = [
    path(
        '', views.index, name='home'
        ),
    path(
        'cats/<int:cat_id>/', views.categories_by_id, name='cats_by_id'
        ),
    path(
        'cats/<slug:cat_slug>/', views.categories_by_slug, name='cats_by_slug'
        ),
    path(
        'archive/<4year:year>/', views.archive, name='archive'
        ),
]