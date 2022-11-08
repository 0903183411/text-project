from re import L
from django.shortcuts import render
import random
from mysite.models import Post

def dbtest(request):
    posts = Post.objects.all()
    return render(request, "dbtest.html", locals())

def lotto(request):
    name = "Jasmine"
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    lotto = sorted(numbers[:6])
    return render(request, "lotto.html", locals())

def index(request):
    name = "Jasmine"
    return render(request, "index.html", locals())

def parttime(request):
    
    return render(request, "parttime.html", locals())