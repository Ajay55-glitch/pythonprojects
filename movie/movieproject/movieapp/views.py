from django.shortcuts import render, redirect
from . models import movie
from . models import Names
from .forms import movieform
# Create your views here.
def index(request):
    result= movie.objects.all()

    return render(request,'index.html', {'result':result})
def detail(request,movie_id):
    result= movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'result':result})
def add_movie(request):
    if request.method=="POST":
        name = request.POST.get('name', )
        img = request.FILES['img']
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        result = movie(name=name,img=img,desc=desc,year=year)
        result.save();

    return render(request,'add.html')

def update(request,id):
    result=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=result)
    if form.is_valid():
        form .save()
        return  redirect('/')
    return render(request,'edit.html',{'result':result,'form':form})

def delete(request,id):
    if request.method=="POST":
            result=movie.objects.get(id=id)
            result.delete()
            return  redirect('/')
    return  render(request,'delete.html')