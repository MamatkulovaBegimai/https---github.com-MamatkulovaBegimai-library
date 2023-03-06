from django.shortcuts import render, redirect
from apps.users.models import User, Liked_product
from django.contrib.auth import authenticate, login
from apps.settings.models import Settings
from django.http.response import HttpResponse
from apps.books.models import Books
# Create your views here.

def register(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create(username = username, email= email)
            user.set_password(password)
            user.save()
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
        return redirect('index')
    context = {
        'setting':setting
    }
    return render(request, 'signup.html', context)

def user_login(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        except:
            return HttpResponse('<h1>Неправильный логин или пароль</h1>')
    context = {
        'setting':setting
    }
    return render(request, 'login.html', context)

def account(request, username):
    setting = Settings.objects.latest('id')
    user = User.objects.get(username = username)
    liked_product = Liked_product.objects.all()
    context = {
        'setting': setting,
        'user': user,
        'liked_product': liked_product,
    }
    
    return render(request, 'account.html', context)

def edit_profile(request, username):
    user = User.objects.get(username = username)
    if request.user != user:
        return redirect('index')
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        if 'update' in request.POST:
            user.username = username
            user.email = email
            user.save()
            return redirect('account', user.username)
        if 'delete' in request.POST:
            user.delete()
            return redirect('register')
          
    context = {
        'setting':setting,
        'user':user,
    }
    return render(request, 'creator-profile-edit.html', context)