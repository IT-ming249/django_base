from django.contrib import admin
from . import views
from django.urls import path
from django.http import HttpResponse

# 指定app名称
app_name = 'movie'

urlpatterns = [
    path("list", views.movie_list,name='movie_list'),
    path("detail/<int:movie_id>", views.movie_detail, name = 'movie_detail')

]