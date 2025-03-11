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

