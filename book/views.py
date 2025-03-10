from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

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

def book_search_detail_str(request,page,name):
    return HttpResponse("名为{},第{}页".format(name,page))

def book_search_detail_slug(request,page):
    return HttpResponse("第{}页".format(page))

def book_search_detail_path(request,page):
    return HttpResponse("第{}页".format(page))

##数据库基本操作相关
#增加book
def add_book(request):
    book1=Book(name="水浒传",author="施耐庵",price=100)
    book1.save()
    return HttpResponse("图书插入成功")
#查找
def query_book(request):
    #books = Book.objects.all() # 查找Book类相对应的表的所有数据
    #books = Book.objects.filter(name="三国演义") ## 数据过滤
    #for book in books:
    #    print(book.name,book.author,book.pub_time,book.price)
    book = Book.objects.get(name="三国演义") #获取单个对象，数据不存在则报错
    print(book.name)
    return HttpResponse("查找成功")

def order_view(request):
    #排序查询
    books = Book.objects.order_by("pub_time") #("-pub_time") 表示倒序查询
    for book in books:
        print(book.name)
    return HttpResponse("排序查询成功")

def modify_book(request):
    book = Book.objects.get(name="水浒传")
    book.price = 99
    book.save()
    return HttpResponse("修改数据成功")

def delete_book(request):
    book = Book.objects.get(id=1)
    book.delete()
    return HttpResponse("删除成功")



