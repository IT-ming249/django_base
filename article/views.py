from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .models import User,Article
# Create your views here.
app_name = 'article'

def article_test(request):
    #插入数据并添加外键
    #user = User(username="明明",password="123456")
    #user.save()
    #article = Article(title="快要毕业了",content="新的人生关卡",author=user)
    #article.save()
    article = Article.objects.first()
    print(article.author.username)  #由于外键的关系 article.author.username就相当与User.username
    return HttpResponse("<h1>Hello World</h1>")

#数据库表与表之间的联系
def one_to_many(request):
    user = User.objects.first()
    #articles = user.article_set.all() #可通过 小写外键模型名_set获取所有外键关联的数据(未设置relate_name)
    articles = user.articles.all()
    for article in articles:
        print(article.title)
    return HttpResponse("一对多")

#数据库查询操作(常用)
def query1(request):
    #精确查询exact,iexact忽略大小写的精确查询
    article = Article.objects.filter(id__exact=1)
    # 查询结果.query可以看到底层执行的sql语句
    print(article.query)
    return HttpResponse("查询成功")

def query2(request):
    #contains判断包含，icontains大小写不敏感
    article = Article.objects.filter(title__contains='快')
    print(article.query)
    return HttpResponse("查询成功")

def query3(request):
    #in指定容器，容器可以是list,tuple或者任何可迭代对象
    article = Article.objects.filter(id__in=[1,2])
    print(article.query)
    print(article)
    return HttpResponse("查询成功")

#补充一些比较简单的规则：gte大于等于 lte小于等于 没有e就没有等于
#startswith 从某个值开始 endwith以某个值结束 前面+i则大小写不敏感

def query4(request):
    #range查询在某一范围内
    start_time = datetime(2025,3,1)
    end_time = datetime(2025,4,1)
    article = Article.objects.filter(pub_time__range=(start_time,end_time))
    print(article.query)
    print(article)
    return HttpResponse("查询成功")

#根据关联的表进行查询
def query5(request):
    #查找发表文章标题中包含"快"的文章的用户
    user = User.objects.filter(articles__title__contains="快")
    print(user.query)
    print(user)
    return HttpResponse("查询成功")