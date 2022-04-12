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
    #dates = stock.date
    #highs = stock.high 
    return render(request, "index.html", locals())

def base(request):
    posts = Post.objects.all()
    return render(request, 'base.html', locals())

    
def prices(request):
    mystock = Stock.objects.all()
    return render(request, "prices.html", locals())

def post(request, cat="",group=""):
    if cat=="":
        mystock = Stock.objects.all()
    else:
        mystock = Stock.objects.filter(cat=cat)
   
    if group=="":
        mystock = Stock.objects.all()
    else:
        mystock = Stock.objects.filter(group=group)
    return render(request, "post.html", locals())




def showdate(request):

    now = datetime.datetime.now()
    return HttpResponse("現在時刻:" + str(now))
