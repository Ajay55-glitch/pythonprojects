from django.shortcuts import render
from django.http import HttpResponse
from .models import place
# Create your views here.
def demo(request):
    result = place.objects.all()
    return render(request,"index.html",{'result': result})

def about(request):
    name='india'
    return  render(request,'about.html',{'obj':name})

def contact(request):
    return  render(request,"contact.html")
def detail(request):
    return  render(request,'detail.html')

def thanks(request):
    return HttpResponse("thanks")

def opperation(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y

    return render(request,'result.html',{'result':add})