from email import message
from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView

import datetime as dt

from .models import Article



# Getting the day of the week
# def convertDates(dates):
#     # Converts date to a day of the week
#     dayNumber = dt.date.weekday(dates)

#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
# # Returning the actual day of the week
#     day = days[dayNumber]
#     return day

# Create your views here.
def searchResult(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'allNews/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'allNews/search.html',{"message":message})
    
def newsOfToday(request):
    date = dt.date.today()
    news = Article.todays_news()
    
    return render(request, 'allNews/today.html', {"date": date, "news":news})

def Pastnews(request, pastDate):
    try:
        # Converts data from the string url
        date = dt.datetime.strptime(pastDate, '%Y-%m-%d').date()
    except ValueError:
        # Raises 404 error when valueError is thrown
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(newsOfToday)
    news = Article.days_news(date)
    return render(request, 'allNews/pastNews.html',{"date": date, "news":news})

def article(request,article_id):
    try:
     article = Article.objects.get(id = article_id)
    except Article.DoesNotExist:
        raise Http404()
    return render(request, 'allNews/article.html', {'article': article})

# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'allNews/article.html'
#     # return render(request, 'allNews/article.html', {'article': article})
