from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, DeleteView

from blogapp.forms import Todoform
from blogapp.models import news


def fun(request):
    obj=news.objects.all()
    return render(request,"news.html",{'results':obj})


class TaskD(DetailView):
    model =news
    template_name ='detail.html'
    context_object_name = 'a'


class TaskU(UpdateView):
    model =news
    template_name ='update.html'
    context_object_name = 'task'
    fields=('name','img','desc','month','date')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})

class Taskd(DeleteView):
    model= news
    template_name = 'delete.html'
    success_url = reverse_lazy('delete')

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        month= request.POST.get('month')
        date= request.POST.get('date')
        img=request.FILES['img']
        s=news(name=name,desc=desc,img=img,month=month,date=date)
        s.save()
        print("product added")
    return render(request,"add.html")

def delete(request,id):
    task=news.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'taask':task})

def update(request,id):
    task=news.objects.get(id=id)
    form=Todoform(request.POST or None,request.FILES,instance=task)
    if form.is_valid():
        form.save();
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})