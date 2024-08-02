from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "4year")

urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories_by_id),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
    path('archive/<4year:year>/', views.archive),
]