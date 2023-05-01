from django.shortcuts import render
from .models import News, Category

def news_list(request):
    news_list = News.objects.all()
    context = {
        "news_list": news_list
    }
    return render(request, 'news/news_list.html', context)

