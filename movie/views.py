from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def movie_list(request):
    return HttpResponse("电影列表")

def movie_detail(request,movie_id):
    return HttpResponse("正在放映{}".format(movie_id))