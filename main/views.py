from django.shortcuts import render
from main.models import todo
from django.http import HttpResponseRedirect
from django.utils import timezone
# Create your views here.
def index(request):
    todo_items = todo.objects.all().order_by('-added_date')
    context = {}

    return render(request,'main/index.html',{
        "todo_items":todo_items
    })
    
def add_todo(request):
    print(request.POST)
    content =request.POST["content"]
    date = timezone.now()
    cobj = todo.objects.create(added_date=date,text=content)
    length = todo.objects.all().count()
    return HttpResponseRedirect("/")

def delete_todo(request,todo_id):
    todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")


