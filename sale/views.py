from django.http import HttpResponse
from django.db.models import Avg, Count, Max, Min, Sum, F, Q
from django.shortcuts import render

from sale.models import Book, Author, BookOrder


# Create your views here.

def sale_index(request):
    return HttpResponse("欢迎来到商城主页")

##数据库聚合函数
def avg_view(request):
    #求平均值
    result = Book.objects.aggregate(Avg('price'))
    print(result)
    return HttpResponse("avg求平均值")

def count_view(request):
    #统计数量
    result = Book.objects.aggregate(Count('id'))
    print(result)
    return HttpResponse("count统计数量")

def max_min_view(request):
    #最大值最小值
    result = Author.objects.aggregate(Max('age'), Min('age'))
    print(result)
    return HttpResponse("最大值最小值")

def sum_view(request):
    #求总和
    result = Book.objects.annotate(total=Sum("bookorder__price")).values("name","total")
    print(result.query)
    print(result)
    return HttpResponse("求和")

##F表达式
def f_view(request):
    #F('price')表示用price原来的值
    Book.objects.update(price=F('price')-10)
    return HttpResponse("F_view")

##Q表达式 并(或)操作
def q_view(request):
    books = Book.objects.filter(Q(price__gte=80) | Q(rating__gte=9)).all()
    for book in books:
        print(book.name)
    return HttpResponse("Q_view")