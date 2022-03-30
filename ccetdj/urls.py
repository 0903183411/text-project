from django.contrib import admin
from django.urls import path
from mysite import views
from mysite.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prices/', views.prices),
    path('post/<slug:slug>/', views.post),
    path('', views.index),
    path('date/', views.showdate),
]
