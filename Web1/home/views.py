from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    msg = 'My First Message'
    return render(request, 'index.html',{'test':'This is New World!!!'})
def error(request):
    raise Http404('Not Found')
