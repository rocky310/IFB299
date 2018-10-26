from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import CarInfo
from .models import HistoryInfo
from .forms import ListForm
from .forms import ListForm1
from .models import Viewcars
from .models import Audi
from .models import Kia
from .models import Hyundai
from .models import Toyota
from .models import Mitsubishi






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

def show_most_rent(request):

    return render(request, 'accounts/show_most_rent.html')

def show_city_orders(request):

    return render(request, 'accounts/show_city_orders.html')

def show_month_orders(request):

    return render(request, 'accounts/show_month_orders.html')

def show_month_orders_2006(request):

    return render(request, 'accounts/show_month_orders_2006.html')

def show_month_orders_2007(request):

    return render(request, 'accounts/show_month_orders_2007.html')


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

def loadnew(request):
    if request.method == 'POST':
        if request.POST['Customer_ID'] and request.POST['Customer_Name'] and request.POST['Order_ID'] and request.POST['Order_CreateDate'] and request.POST['Order_PickupDate'] and request.POST['Order_Pickup_Store'] and request.POST['Pickup_Store_Name'] and request.POST['Order_ReturnDate'] and request.POST['Order_ReturnStore'] and request.POST['Return_Store_Name'] and request.POST['Car_ID'] and request.POST['Car_MakeName'] and request.POST['Car_Model'] and request.POST['Car_Series'] and request.POST['Car_SeriesYear']:
            product = CarInfo()
            product.Customer_ID = request.POST['Customer_ID']
            product.Customer_Name = request.POST['Customer_Name']
            product.Order_ID = request.POST['Order_ID']
            product.Order_CreateDate = request.POST['Order_CreateDate']
            product.Order_PickupDate = request.POST['Order_PickupDate']
            product.Order_Pickup_Store = request.POST['Order_Pickup_Store']
            product.Pickup_Store_Name = request.POST['Pickup_Store_Name']
            product.Order_ReturnDate = request.POST['Order_ReturnDate']
            product.Order_ReturnStore = request.POST['Order_ReturnStore']
            product.Return_Store_Name = request.POST['Return_Store_Name']
            product.Car_ID = request.POST['Car_ID']
            product.Car_MakeName = request.POST['Car_MakeName']
            product.Car_Model = request.POST['Car_Model']
            product.Car_Series = request.POST['Car_Series']
            product.Car_SeriesYear = request.POST['Car_SeriesYear']
            product.save()
            messages.success(request, ('New information has been added!'))
            return redirect('record')
        else:
            messages.success(request, ('All fields are required!'))
            return redirect('loadnew')
    else:
        return render(request, 'accounts/loadnew.html')


def delete(request, id):
    item_delete = CarInfo.objects.get(pk=id)
    item_delete.delete()
    messages.success(request, ('The Information Has Been Deleted!'))
    return redirect('record')


def edit(request, id):
    if request.method == 'POST':
        item_edit = CarInfo.objects.get(pk=id)
        form = ListForm(request.POST or None, instance=item_edit)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Information Has Been Edited!'))
            return redirect('record')

    else:
        item_edit = CarInfo.objects.get(pk=id)
        return render(request, 'accounts/edit.html', {'item': item_edit})

def addcars(request):
    if request.method == 'POST':
        if request.POST['Car_MakeName'] and request.POST['Car_Series'] and request.POST['Car_SeriesYear'] and request.POST['Car_EngineSize'] and request.POST['Car_FuelSystem'] and request.POST['Car_TankCapacity'] and request.POST['Car_Power'] and request.POST['Car_SeatingCapacity'] and request.POST['Car_BodyType'] and request.POST['Car_Drive'] and request.FILES['image']:
            product = Viewcars()
            product.Car_MakeName = request.POST['Car_MakeName']
            product.Car_Series = request.POST['Car_Series']
            product.Car_SeriesYear = request.POST['Car_SeriesYear']
            product.Car_EngineSize = request.POST['Car_EngineSize']
            product.Car_FuelSystem = request.POST['Car_FuelSystem']
            product.Car_TankCapacity = request.POST['Car_TankCapacity']
            product.Car_Power = request.POST['Car_Power']
            product.Car_SeatingCapacity = request.POST['Car_SeatingCapacity']
            product.Car_BodyType = request.POST['Car_BodyType']
            product.image = request.FILES['image']
            product.save()
            messages.success(request, ('New information has been added!'))
            return redirect('addcars')
        else:
            messages.success(request, ('All fields are required!'))
            return redirect('addcars')
    else:
        return render(request, 'accounts/addcars.html')


def viewcars(request):
    cars = Viewcars.objects.all()
    return render(request, 'accounts/viewcars.html', {'cars': cars})


def view_audi(request):
    cars = Audi.objects.all()
    return render(request, 'accounts/view_audi.html', {'cars': cars})

def view_kia(request):
    cars = Kia.objects.all()
    return render(request, 'accounts/view_kia.html', {'cars': cars})

def view_toyota(request):
    cars = Toyota.objects.all()
    return render(request, 'accounts/view_toyota.html', {'cars': cars})

def view_mitsubishi(request):
    cars = Mitsubishi.objects.all()
    return render(request, 'accounts/view_mitsubishi.html', {'cars': cars})

def view_hyundai(request):
    cars = Hyundai.objects.all()
    return render(request, 'accounts/view_hyundai.html', {'cars': cars})


def viewmore(request, id):
    if request.method == 'POST':
        viewmore = Viewcars.objects.get(pk=id)
        form = ListForm1(request.POST or None, instance=viewmore)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Information Has Been Edited!'))
            return redirect('viewmore')

    else:
        viewmore = Viewcars.objects.get(pk=id)
        return render(request, 'accounts/viewmore.html', {'viewmore': viewmore})

def audi_viewmore(request, id):
    if request.method == 'POST':
        viewmore = Audi.objects.get(pk=id)
        form = ListForm1(request.POST or None, instance=viewmore)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Information Has Been Edited!'))
            return redirect('audi_viewmore')

    else:
        viewmore = Audi.objects.get(pk=id)
        return render(request, 'accounts/audi_viewmore.html', {'viewmore': viewmore})

def kia_viewmore(request, id):
    if request.method == 'POST':
        viewmore = Kia.objects.get(pk=id)
        form = ListForm1(request.POST or None, instance=viewmore)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Information Has Been Edited!'))
            return redirect('kia_viewmore')

    else:
        viewmore = Kia.objects.get(pk=id)
        return render(request, 'accounts/kia_viewmore.html', {'viewmore': viewmore})

def hyundai_viewmore(request, id):
    if request.method == 'POST':
        viewmore = Hyundai.objects.get(pk=id)
        form = ListForm1(request.POST or None, instance=viewmore)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Information Has Been Edited!'))
            return redirect('hyundai_viewmore')

    else:
        viewmore = Hyundai.objects.get(pk=id)
        return render(request, 'accounts/hyundai_viewmore.html', {'viewmore': viewmore})

def mitsubishi_viewmore(request, id):
    if request.method == 'POST':
        viewmore = Mitsubishi.objects.get(pk=id)
        form = ListForm1(request.POST or None, instance=viewmore)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Information Has Been Edited!'))
            return redirect('mitsubishi_viewmore')

    else:
        viewmore = Mitsubishi.objects.get(pk=id)
        return render(request, 'accounts/mitsubishi_viewmore.html', {'viewmore': viewmore})

def toyota_viewmore(request, id):
    if request.method == 'POST':
        viewmore = Toyota.objects.get(pk=id)
        form = ListForm1(request.POST or None, instance=viewmore)
        if form.is_valid():
            form.save()
            messages.success(request, ('The Information Has Been Edited!'))
            return redirect('toyota_viewmore')

    else:
        viewmore = Toyota.objects.get(pk=id)
        return render(request, 'accounts/toyota_viewmore.html', {'viewmore': viewmore})