from django.http import HttpResponse
from .forms import MessageBoardForm, RegisterForm, ArticleForm
from django.shortcuts import render
#请求验证装饰器
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        form = MessageBoardForm()
        return render(request, 'form_index.html',context={'form':form})
    else:
        #post请求提交上来的数据，需要验证表单
        form = MessageBoardForm(request.POST)
        #表单验证通过↓
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            email = form.cleaned_data['email']
            return HttpResponse(f"{title},{content},{email}")
        else:
            print(form.errors)
            return HttpResponse("提交数据有误")

@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            return HttpResponse(telephone)
        else:
            print(form.errors)
            return HttpResponse("表单验证失败！")

@require_http_methods(['GET', 'POST'])
def article_view(request):
    if request.method == 'GET':
        return render(request,"article.html")
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            return HttpResponse(f"{title},{content}")
        else:
            print(form.errors)
            return HttpResponse("表单验证失败")