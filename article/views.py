from django.shortcuts import render
from .models import Article

def home(request):
    posts = Article.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'article/home.html', context)

def contact(request):
    return render(request, 'article/contacts.html')

