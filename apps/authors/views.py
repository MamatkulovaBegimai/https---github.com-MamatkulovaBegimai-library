from django.shortcuts import render
from apps.authors.models import Authors
from apps.settings.models import Settings
from apps.books.models import Books
# Create your views here.
def authors(request):
    authors = Authors.objects.all()
    setting = Settings.objects.latest('id')
    random_products = Books.objects.order_by('?')[:3]

    context = {
        'authors': authors,
        'setting': setting,
        'random_products': random_products
        
    }
    return render(request, 'authors.html', context)

def authors_detail(request, id):
    setting = Settings.objects.latest('id')
    authors = Authors.objects.all()
    authors_detail = Authors.objects.get(id = id)
    books = Books.objects.all()
    context = {
        'authors_detail': authors_detail,
        'authors': authors,
        'setting': setting,
        'books': books,
    }
    return render(request, 'authordetail.html', context)

