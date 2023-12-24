from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    stores = Store.objects.all()
    clients = Client.objects.all()
    return render(request, 'dashboard.html', {'stores': stores, 'clients': clients})


@login_required(login_url='login')
def jewelry(request):
    items = Jewelry.objects.all()
    return render(request, 'jewelry.html', {'items':items})


@login_required(login_url='login')
def createJewelry(request):
    form = JewelryForm()
    if request.method=='POST':
        form = JewelryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/jewelry')

    context = {'form': form}
    return render(request, 'jewelry_form.html', context)


@login_required(login_url='login')
def updateJewelry(request, pk):
    jewelry = Jewelry.objects.get(id=pk)
    form = JewelryForm(instance=jewelry)
    if request.method=='POST':
        form = JewelryForm(request.POST, instance=jewelry)
        if form.is_valid():
            form.save()
            return redirect('/jewelry')
    context ={'form': form}
    return render(request, 'jewelry_form.html', context)


@login_required(login_url='login')
def deleteJewelry(request, pk):
    jewelry = Jewelry.objects.get(id=pk)
    if request.method == 'POST':
        jewelry.delete()
        return redirect('/jewelry')
    context = {'item': jewelry}
    return render(request, 'delete_jewelry.html', context)


@login_required(login_url='login')
def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


@login_required(login_url='login')
def createClient(request):
    form = ClientForm()
    if request.method=='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clients')

    context = {'form': form}
    return render(request, 'clients_form.html', context)


@login_required(login_url='login')
def updateClient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method=='POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/clients')
    context ={'form': form}
    return render(request, 'clients_form.html', context)


@login_required(login_url='login')
def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/clients')
    context = {'item': client}
    return render(request, 'delete_client.html', context)


@login_required(login_url='login')
def stores(request):
    stores = Store.objects.all()
    return render(request, 'stores.html', {'stores': stores})


@login_required(login_url='login')
def createStore(request):
    form = StoreForm()
    if request.method=='POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/stores')

    context = {'form': form}
    return render(request, 'store_form.html', context)


@login_required(login_url='login')
def updateStore(request, pk):
    store = Store.objects.get(id=pk)
    form = StoreForm(instance=store)
    if request.method=='POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('/stores')
    context ={'form': form}
    return render(request, 'store_form.html', context)


@login_required(login_url='login')
def deleteStore(request, pk):
    store = Store.objects.get(id=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('/stores')
    context = {'item': store}
    return render(request, 'delete_store.html', context)


@login_required(login_url='login')
def profile(request):
    return HttpResponse('Profile')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account successfully created')
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, "Username or password is incorrect")
        context={}
        return render(request, 'login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

