from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def home(request):
    todo_objs = Todo.objects.all()
    data = {'todos':todo_objs}
    return render(request,'index.html',context=data)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Todo.objects.create(name=name,description=description,status=status)
        return redirect('home')
    return render(request,'create.html')

def editpage(request):
    todo_objs = Todo.objects.all()
    data = {'todos':todo_objs}
    return render (request,'editpage.html',context=data)

def edit(request,pk):
    todo_edit = Todo.objects.get(id = pk)
    if request.method== 'POST':
        todo_edit.name = request.POST.get('name')
        todo_edit.description = request.POST.get('description')
        todo_edit.status = request.POST.get('status')
        todo_edit.save()
        return redirect('home')
    new_data = {'todo':todo_edit}
    return render(request,'edit.html',context=new_data)

def deletepage(request):
    todo_objs = Todo.objects.all()
    data = {'todos':todo_objs}
    return render (request,'deletepage.html',context=data)

def delete(request,pk):
    todo_obj = Todo.objects.get(id = pk)
    todo_obj.delete()
    return redirect('home')
