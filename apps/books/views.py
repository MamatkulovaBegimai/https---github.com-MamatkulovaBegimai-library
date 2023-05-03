from django.shortcuts import render, redirect
from apps.books.models import Books, Category
from apps.settings.models import Settings
from apps.authors.models import Authors
from apps.users.models import Liked_product
from django.http import FileResponse

# Create your views here.
def products(request):
    random_products = Books.objects.order_by('?')[:3]
    setting = Settings.objects.latest('id')
    random_authors = Authors.objects.order_by('?')[:3]
    new_book = Books.objects.latest('id')
    categoriies = Category.objects.all()
    products = Books.objects.all()
    context = {
        'setting': setting,
        'random_authors': random_authors,
        'new_book': new_book,
        'categoriies': categoriies,
        'random_products': random_products,
        'products': products
    }
    return render(request, 'products.html', context)

def products_detail(request, id):
    products_detail = Books.objects.get(id = id)
    setting = Settings.objects.latest('id')
    random_products = Books.objects.order_by('?')[:3]
    random_authors = Authors.objects.order_by('?')[:3]
    products = Books.objects.all()
    new_book = Books.objects.latest('id')
    categoriies = Category.objects.all()
    product = Books.objects.get(id=id)
    if request.method == 'POST':
        if 'like' in request.POST:
            try:
                liked_product = Liked_product.objects.get(product = product, user = request.user)
                liked_product.delete()
                return redirect('products_detail', product.id)
            except:
                liked_product = Liked_product.objects.create(product = product, user = request.user)
                liked_product.save()
                return redirect('products_detail', product.id)     
   
        if 'download' in request.POST:
            return FileResponse(products_detail.book_pdf, as_attachment=True)
    
    context = {
        'products_detail': products_detail,
        'setting': setting,
        'random_products': random_products,
        'random_authors': random_authors,
        'products': products,
        'new_book': new_book,
        'categoriies': categoriies,


    }
    return render(request, 'productdetail.html', context)

def category_book(request, slug):
    products = Books.objects.all()
    categoriies = Category.objects.all()
    categories = Category.objects.get(slug = slug)
    setting = Settings.objects.latest('id')
    context = {
        'categories': categories,
        'setting': setting,
        'products': products,
        'categoriies': categoriies,
    }
    return render(request, 'categories/category_detail.html', context)


