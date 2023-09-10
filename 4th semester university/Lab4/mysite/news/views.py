from django.shortcuts import render
from .models import News


def news_list(request):
    # news_list2 = News.objects.all()
    # context = {
    #     'news_list': news_list2,
    # }
    # return render(request, 'news/news_list.html', context)
    return render(request, '')
