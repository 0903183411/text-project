from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=10)  #股票名稱
    sid = models.CharField(max_length=10)   #股票代號
    price = models.FloatField(default=0.0)  #收盤價
    date = models.DateField()               #日期

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.name
