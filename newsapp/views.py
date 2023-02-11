from django.shortcuts import render, HttpResponse, redirect
from newsapp.forms import NewsForm

# Create your views here.
def news(request):
    newsAll = createNews.objects.all()
    return render(request, 'news.html', {'news': newsAll})

def createNews(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        #context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsForm()
        context = {'newsForm': form}
    return render(request, 'news.html', context)

def updateNews(request):
    return render(request, 'update news.html')

def deleteNews(request):
    return render(request, 'delete news.html')