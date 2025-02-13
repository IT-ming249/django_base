from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def movie_index(request):
    return render(request,'movie_index.html')
def movie_list(request):
    return HttpResponse("电影列表")

def movie_detail(request,movie_id):
    return HttpResponse("正在放映{}".format(movie_id))

#模板变量渲染
def movie_info(request,movie_id):
    # 普通变量
    username = 'minming'
    #字典变量
    m_book = {'name':'naza2','author':'lising'}
    #列表变量
    ref_books = [
        {'name':'西游记','author':'罗贯中'},
        {'name':'哪吒闹海','authof':'bzd'}
    ]
    #对象
    class Person:
        def __init__(self,realname):
            self.realname = realname
    context = {
        'username':username,
        'm_book':m_book,
        'ref_books':ref_books,
        'Person':Person('和灏明')
    }
    return render(request,'info.html',context=context)