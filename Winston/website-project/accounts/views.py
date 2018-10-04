from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import CarInfo
from .models import HistoryInfo
from .forms import ListForm


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('manager')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('manager')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
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
    items = CarInfo.objects.all()
    return render(request, 'accounts/manager.html', {'items': items})


def browser(request):
    items = CarInfo.objects.all()
    return render(request, 'accounts/browser.html', {'items': items})


def record(request):
    items = CarInfo.objects.all()
    return render(request, 'accounts/record.html', {'items': items})


def history(request):
    items = HistoryInfo.objects.all()
    return render(request, 'accounts/history.html', {'items': items})


def test(request):
    items = CarInfo.objects.all()
    return render(request, 'accounts/test.html', {'items': items})

def test2(request):
    return render(request, 'accounts/test2.html')


def delete(request, id):
    item_delete = CarInfo.objects.get(pk=id)
    item_delete.delete()
    messages.success(request, ('The Information Has Been Deleted!'))
    return redirect('test')


def edit(request, id):
    if request.method == 'POST':
        item_edit = CarInfo.objects.get(pk=id)
        form = ListForm(request.POST or None, instance=item_edit)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Information Has Been Edited!'))
            return redirect('test')

    else:
        item_edit = CarInfo.objects.get(pk=id)
        return render(request, 'accounts/edit.html', {'item': item_edit})
