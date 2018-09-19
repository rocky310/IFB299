from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import CarInfo

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('manager')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('manager')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def portfolio(request):
    return render(request, 'accounts/portfolio.html')

def customer(request):
    return render(request, 'accounts/customer.html')

def manager(request):
    return render(request, 'accounts/manager.html')

def browser(request):
    return render(request, 'accounts/browser.html')

def record(request):
    return render(request, 'accounts/record.html')

def history(request):
    return render(request, 'accounts/history.html')


def test(request):
    items = CarInfo.objects.all()
    return render(request, 'accounts/test.html',{'items':items})
# return render(request, 'accounts/test.html')
