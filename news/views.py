from django.shortcuts import render

# Create your views here.
def mynews(request):
    newsall='Demo News, Welcome to news page'
    data={
        'newsall':newsall
    }
    return render(request,'news.html',data)