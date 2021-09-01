from django.http import response
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import Search
import datetime
from datetime import date, timedelta

# Create your views here.
def search(request):
    user = get_user_model()
    users = user.objects.all()
    keywords = Search.objects.all()
    # Entry.objects.filter(headline="Test")
    # Search.objects.filter(date__year='2020', 
    #                   date__month='01')
    # startdate = date.today()
    # enddate = startdate + timedelta(days=6)
    # Sample.objects.filter(date__range=[startdate, enddate])

    Search.objects.filter(date__range=["2011-01-01", "2011-01-31"])
    Search.objects.filter(date__year='2011', 
                      date__month='01')
    data = {
        'users' : users,
        'keywords': keywords
    }
    return render(request, 'index.html', data)