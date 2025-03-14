from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("cookie session demo")

#一般来说不会直接操作cookie,下面的操作就是体验一下
def add_cookie(request):
    response = HttpResponse("设置cookie")
    #max_age过期时间的单位是 秒
    response.set_cookie("username","it_ming",max_age=3600)
    return response

def delete_cookie(request):
    response = HttpResponse("删除cookie")
    response.delete_cookie("username")
    return response

def get_cookie(request):
    #username = request.COOKIES.get("username")
    #print(username)
    for key, value in request.COOKIES.items():
        print(key, value)
    return HttpResponse("获取cookie")

##django中的session默认存储在服务器的数据库中，在表中会根据sessionid来提取指定的session数据，sessioni会放到cookie中发送给浏览器存储

def add_session(request):
    # 若没设置过期时间，则采用默认过期时间，两周
    request.session["username"] = "it_ming"
    # 过期时间单位为秒，0则表示关闭浏览器就过期，可根据这个特性开发"记住我"功能
    request.session.set_expiry(0)
    return HttpResponse("session add")

def get_session(request):
    username = request.session.get("username")
    print(username)
    request.session.clear_expired()  #清理过期的session
    return HttpResponse("get session")