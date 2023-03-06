from django.urls import path
from apps.books.views import products, products_detail, category_book
urlpatterns = [
    path('category_book/<str:slug>/', category_book, name='category_book'),
    path('', products, name='products'),
    path('products_detail/<int:id>/', products_detail, name='products_detail'), 
]   