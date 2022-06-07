from email import message
from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from rest_framework import status


from rest_framework.response import Response
from rest_framework.views import APIView

import datetime as dt

from .models import *
from .forms import *
from .email import *
from .serializer import MerchSerializer


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
    nform = NewsLetterForm(request.POST)

    # Adding the form:

    if request.method == 'POST':
        if nform.is_valid():
            name = nform.cleaned_data['name']
            email = nform.cleaned_data['email']
            Subscriber =  Subscribers(name = name, email = email)
            Subscriber.save()
            send_welcome_email(name, email)
            HttpResponseRedirect('newsOfToday')
            # print('valid')
        else:
            nform=NewsLetterForm()

    
    return render(request, 'allNews/today.html', {"date": date, "news":news, "nForm": nform})

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

@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('NewsOfToday')
    else:
        form = NewArticleForm()
    return render(request, 'news', new_article.html,{"form": form})


class MerchList(APIView): # inherits from the APIView class.
    def get (self, request, format=None):
        all_merch = MoringaMerch.objects.all() # query the database to get all the MoringaMerchobjects. 
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
