from django.shortcuts import render, redirect
from apps.settings.models import Settings, Aboutus, Team, Otklic
from apps.authors.models import Authors
from apps.books.models import Books, Category
from django.db.models import Q
from apps.users.models import User
from django.core.mail import send_mail


# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    authors = Authors.objects.all()
    products = Books.objects.all()
    categoriies = Category.objects.all()
    new_book = Books.objects.latest('id')
    user = User.objects.all()
    random_products = Books.objects.order_by('?')[:3]
    random_authors = Authors.objects.order_by('?')[:3]
    context = {
        'setting':setting,
        'authors':authors,
        'products': products, 
        'categoriies': categoriies,
        'new_book': new_book,
        'user': user,
        'random_products': random_products,
        'random_authors': random_authors,
    }
    return render(request, 'index.html', context)

def aboutus(request):
    aboutus = Aboutus.objects.latest('id')
    setting = Settings.objects.latest('id')
    team = Team.objects.all()
    categoriies = Category.objects.all()
    context = {
        'setting':setting,
        'aboutus': aboutus,
        'team': team,
        'categoriies': categoriies,
    }
    return render(request, 'aboutus.html', context)

def search(request):
    products = Books.objects.all()
    authors = Authors.objects.all()
    setting = Settings.objects.latest('id')
    search_key = request.GET.get('key')
    if search_key:
        products = Books.objects.filter(Q(name__icontains = search_key))
        authors = Authors.objects.filter(Q(name__icontains = search_key))
    context = {
        'setting':setting,
        'products': products,
        'authors': authors
    }
    return render(request,'search.html', context)

def response(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        otklic = Otklic.objects.create(full_name = name, email = email, phone = phone, subject = subject, text = message)
        otklic.save()
        send_mail(
            #subject 
            f"Спасибо за отклик: {subject}", 
            #message 
            f"Здравствуйте {name}, спасибо за отклик мы с вами свяжемся.", 
            #from email 
            'begimaimamatkulova7@gmail.com', 
            #to email 
            [email] 
        )
        return redirect('index')
    context = {
        'setting' : setting,
    }
    return render (request, 'contactus.html', context)