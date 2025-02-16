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