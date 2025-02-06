from django.shortcuts import render
from django.http import HttpResponse

#带参数的url示例
#http://127.0.0.1:8000/book?id=3&name=mm
def book_search_id(request):
    #↓从request中拿到id
    book_id = request.GET.get('id')
    name = request.GET.get('name')
    return HttpResponse("您好{}您查找的id是{}".format(name,book_id))

##http://127.0.0.1:8000/book/1
def book_search_detail_int(request,page):
    return HttpResponse("第{}页".format(page))

def book_search_detail_str(request,page):
    return HttpResponse("第{}页".format(page))

def book_search_detail_slug(request,page):
    return HttpResponse("第{}页".format(page))

def book_search_detail_path(request,page):
    return HttpResponse("第{}页".format(page))