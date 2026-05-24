from django.shortcuts import render
from news.models import News

# Create your views here.
def mynews(request):
    newsall=News.objects.all().order_by('news_title')
    data={
        'newsall':newsall
    }
    return render(request,'news.html',data)

def NewsDetails(request,n_id):
    Newsdetails=News.objects.get(id=n_id)
    data={
        'Newsdetails':Newsdetails
    }
    return render(request,'news.html',data)