from django.urls import path
from apps.authors.views import authors, authors_detail

urlpatterns = [
    path('', authors, name='authors'),
    path('authors_detail/<int:id>/', authors_detail, name='authors_detail' ),
]    