from django.shortcuts import render
from news.models import News
from .models import Milliseconds


def home(request):
    if request.method == 'POST' and 'new_number' in request.POST:
        Milliseconds.set_static_variable(request.POST["number"])

    context = {
        'latest_article': News.objects.latest('publication_date'),
        'miliseconds': str(Milliseconds.get_static_variable()),
    }
    return render(request, 'main.html', context)
