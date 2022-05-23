from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt


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
    # Function that converts date object to find day:
    day = convertDates(date) 
    html = f'''
        <html>
            <body>
                <h1> Moringa Tribune</h1>
                <h3>News for {day} {date.day}-{date.month}-{date.year}</h3>
                <h6>by AtienoObwanda </h6>
            </body>
        </html>
            '''
    return HttpResponse(html)

def Pastnews(request, pastDate):
    try:
        # Converts data from the string url
        date = dt.datetime.strptime(pastDate, '%Y-%m-%d').date()
    except ValueError:
        # Raises 404 error when valueError is thrown
        raise Http404()

