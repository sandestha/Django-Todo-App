from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Todo

# Create your views here.
def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            HttpResponse('Invalid Credentials')
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

def Login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(request,username = uname,password = passwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            HttpResponse('Invalid Username or Password')
    return render(request,'login.html')


@login_required(login_url='login')
def home(request):
    todo_objs = Todo.objects.all()
    data = {'todos':todo_objs}
    return render(request,'index.html',context=data)


@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Todo.objects.create(name=name,description=description,status=status)
        return redirect('home')
    return render(request,'create.html')


@login_required(login_url='login')
def editpage(request):
    todo_objs = Todo.objects.all()
    data = {'todos':todo_objs}
    return render (request,'editpage.html',context=data)

@login_required(login_url='login')
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


@login_required(login_url='login')
def deletepage(request):
    todo_objs = Todo.objects.all()
    data = {'todos':todo_objs}
    return render (request,'deletepage.html',context=data)

@login_required(login_url='login')
def delete(request,pk):
    todo_obj = Todo.objects.get(id = pk)
    todo_obj.delete()
    return redirect('home')

def Logout(request):
    logout(request)
    return redirect('login')