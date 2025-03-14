from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
# Create your views here.

def index(request):
    return HttpResponse("csrf index")

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print(request.POST)
        print(request.COOKIES)
        return HttpResponse("csrf login")
