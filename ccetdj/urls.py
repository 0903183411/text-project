from django.contrib import admin
from django.urls import path
from mysite import views
from mysite.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prices/', views.prices),
    path('post/', views.post),
    path('post/<str:cat>/', views.post),
    path('', views.index),
    path('date/', views.showdate),
]
