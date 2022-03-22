from cgitb import html
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import datetime, twstock
from mysite.models import Stock

def index(request):
    
    now = datetime.datetime.now()
    #stock = twstock.Stock('2330')
    #prices = stock.price
    # dates = stock.date
    #highs = stock.high 
    mystock = stock.objects.all()
    return render(request, "index.html", locals())
    

def showdate(request):

    now = datetime.datetime.now()
    return HttpResponse("現在時刻:" + str(now))
