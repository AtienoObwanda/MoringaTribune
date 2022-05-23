from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
import datetime as dt

from .models import Article



# Getting the day of the week
def convertDates(dates):
    # Converts date to a day of the week
    dayNumber = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
# Returning the actual day of the week
    day = days[dayNumber]
    return day

# Create your views here.
def welcome(request):
    # return HttpResponse('Welcome to the Moringa Tribune by AtienoObwanda')
    return render(request, 'index.html')
    
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

