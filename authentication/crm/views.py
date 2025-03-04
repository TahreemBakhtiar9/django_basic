from django.shortcuts import render, redirect
from . forms import CreateUserFrom, LoginForm
# from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def homepage(request):
    
    # return HttpResponse("This is the Homepage")
    return render(request, 'crm/index.html')


def register(request):
    form = CreateUserFrom()
    
    if request.method == "POST":
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    
    context = {'registerform': form}   
    return render(request, 'crm/register.html', context=context)


def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    
    context = {'loginform':form}
    return render(request, 'crm/my-login.html', context=context)


def user_logout(request):
    auth.logout(request)
    return redirect("")

@login_required(login_url="my-login")
def dashboard(request):
    
    return render(request, 'crm/dashboard.html')