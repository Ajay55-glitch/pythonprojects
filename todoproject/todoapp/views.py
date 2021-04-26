from django.shortcuts import render,redirect
from .models import Task
from .forms import todoform
from django.views.generic import  ListView

class tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'


# Create your vi
def add(request):
    task=Task.objects.all()
    if request.method=="POST":
        name = request.POST.get('task', )

        priority = request.POST.get('priority', )
        date = request.POST.get('date', )

        result =Task(name=name,priority=priority,date=date)
        result.save();

    return render(request,'home.html',{'task':task})


def delete(request,id):
    if request.method=="POST":
            result=Task.objects.get(id=id)
            result.delete()
            return  redirect('/')
    return  render(request,'delete.html')


def update(request,id):
    result=Task.objects.get(id=id)
    form=todoform(request.POST or None,instance=result)
    if form.is_valid():
        form .save()
        return  redirect('/')
    return render(request,'edit.html',{'result':result,'form':form})
