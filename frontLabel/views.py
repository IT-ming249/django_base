from datetime import datetime
import datetime
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def if_label(request):
    age = 18
    context = {'age': age}
    return render(request,'if.html',context=context)

def for_in_label(requset):
    ref_books = [
        {'name': '西游记', 'author': '罗贯中'},
        {'name': '哪吒闹海', 'author': 'bzd'}
    ]

    person = {
        'id': 1,
        'name':'mmg',
        'age':18
    }
    context = {
        'ref_books': ref_books,
        'person': person
    }
    return render(requset,'for_in.html',context=context)

def with_label(requset):
    #with标签适合经常访问且访问方式比较麻烦的变量
    context = {
        "ref_books":[
        {'name': '西游记', 'author': '罗贯中'},
        {'name': '哪吒闹海', 'author': 'bzd'}
    ]
    }
    return render(requset,"with.html",context=context)

def url_label(request):
    return render(request,"url.html")

#过滤器
def filter(request):
    greet = "hello , django !"
    date = datetime.datetime.now()
    profile = ""
    context = {
        "greet":greet,
        "date":date,
        "profile":profile
    }
    return render(request,"filter.html",context=context)

def include_html_model(request):
    context={
        "papers":["IMM","CCP","SDR"],
    }
    return render(request,"paper_index.html",context=context)

def static_example(request):
    return render(request,"static.html")