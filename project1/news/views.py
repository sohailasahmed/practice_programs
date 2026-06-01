from django.shortcuts import render
from news.models import News

# Create your views here.
def mynews(request):
    newsall=News.objects.all().order_by('news_title')
    data={
        'newsall':newsall
    }
    return render(request,'news.html',data)

def NewsDetails(request,slug):
    Newsdetails = News.objects.get(news_slug=slug)
    data={
        'Newsdetails':Newsdetails
    }
    return render(request,'news.html',data)

