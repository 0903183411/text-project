from cgitb import html
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
#from .models import ToDoList, Item
import datetime

def index(request):
    html = "<h2>Hello</h2><hr>"
    now = datetime.datetime.now()
    html = html + "現在時刻:" + str(now)
    return HttpResponse(html)
 
def showdate(request):

    now = datetime.datetime.now()
    return HttpResponse("現在時刻:" + str(now))

def index(response, id):
    #Is = ToDoList.objects.get(id = id)
    return render(response,"base.html",{})
