from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('', views.index),
    path('dbtest/', views.dbtest),
    path('lotto/', views.lotto),
    path('admin/', admin.site.urls),
    path('parttime',views.parttime),
]