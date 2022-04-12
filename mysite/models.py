from django.db import models
from django.shortcuts import render
from django.http import HttpResponse




class Stock(models.Model):
    name = models.CharField(max_length=10)  #股票名稱
    sid = models.CharField(max_length=10)   #股票代號
    cat = models.CharField(max_length=4, default='10')    #股票所屬的類別
    price = models.FloatField(default=0.0)  #收盤價
    date = models.DateField()               #日期
    high = models.FloatField(default=0.0)   #最高價
    group = models.CharField(max_length=4)    #股票所屬的族群
    
    

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.name


    