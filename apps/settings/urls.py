from django.urls import path, include
from apps.settings.views import index, aboutus, search, response

urlpatterns = [
    path('', index, name='index'),
    path('aboutus/', aboutus, name='aboutus'),
    path('search/', search, name='search'),
    path('response/', response, name='response'),

]
