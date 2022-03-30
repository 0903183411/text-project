from django.contrib import admin
from mysite.models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'sid', 'cat', 'price', 'date', 'high')
