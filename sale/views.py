from django.http import HttpResponse
from django.db.models import Avg, Count, Max, Min, Sum
from django.shortcuts import render

from sale.models import Book, Author, BookOrder


# Create your views here.

def sale_index(request):
    return HttpResponse("欢迎来到商城主页")

#数据库聚合函数
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