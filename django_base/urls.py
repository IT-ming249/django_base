"""
URL configuration for django_base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include ,reverse
from django.http import HttpResponse
from book import views
from django.shortcuts import render
#数据库连接相关依赖↓
from django.db import connection

#定义一个简单的视图函数
def index(request):
    #路由反转不带参
    #print(reverse('index'))
    #print(reverse('book'))

    #路由反转带参
    #print(reverse('book_int', kwargs={'page':1}))
    #查询字符串传参
    #print(reverse('book') + '?id=1')

    #命名空间下的路由反转
    #print(reverse("movie:movie_index"))
    #print(reverse('movie:movie_list'))
    #print(reverse('movie:movie_detail', kwargs={'movie_id':1}))

    ##测试数据库连接
    """"
    #获取游标对象
    cursor = connection.cursor()
    #拿到游标后执行SQL语句
    cursor.execute("select * from book")
    #获取所有数据
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    """
    return render(request, "index.html")
"""
path函数
path(route,views,name=None,Kwargs=None)
route参数使用<>传递参数可限定为int,str,slug,path类型，str是默认类型
int表示限制类型,若是str类型则不能包含斜杠/,slug是由中文横杠-,或下划线_连接的也问字符或者数字组成的字符串
path是包含斜杠的字符串
view参数表示视图函数
name参数 给url取名字，url反转的时候有大用处
"""

urlpatterns = [
    path("admin/", admin.site.urls),
    # http://127.0.0.1:8000/s  访问index视图函数 ↓
    path("",index, name = 'index'),
    #↓是book这个app的url，未模块化
    #http://127.0.0.1:8000/book?id=3&name=mm ↓
    path("book", views.book_search_id, name = 'book'),
    #http://127.0.0.1:8000/book/1 ↓
    path("book/int/<int:page>", views.book_search_detail_int, name = 'book_int'),
    path("book/str/<name>/<int:page>", views.book_search_detail_str, name = 'book_str'),
    path("book/slug/<slug:page>", views.book_search_detail_slug, name = 'book_slug'),
    path("book/path/<path:page>", views.book_search_detail_path, name = 'book_path'),
    path("book/add",views.add_book, name = 'book_add'),
    path("book/query",views.query_book, name = 'book_query'),
    path("book/order",views.order_view, name = 'book_order'),
    path("book/modify",views.modify_book, name = 'book_modify'),
    path("book/delete",views.delete_book, name = 'book_delete'),

    #模块化导入：include方法导入movie相关的url, ↓表示所有movie/打头的url都去读取movie.urls中的path
    path('movie/', include('movie.urls')),
    path('frontLabel/', include('frontLabel.urls')),
]
