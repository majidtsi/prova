from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PrenotaForm, OrdineForm
from .models import Category, Piatti, Cliente, Reservation, Ordini
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


"""
def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
"""
def index(request):
    cat=Piatti.objects.all()
    context={'piat':cat}
    return render(request,'index.html',context=context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)

@login_required
def prenota(request):
    if request.method=='POST':
        form = PrenotaForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save()
            print("ok")
            cliente=Cliente.objects.get(user=request.user)
            preno=Reservation.objects.get(id=myform.id)
            cliente.reservation=preno
            cliente.save()
            ord=Ordini()
            ord.cliente=cliente
            ord.prenota=preno

            ord.save()

            return redirect('ordine')

    else:
        form = PrenotaForm()

    return render(request,'prenota.html',{'form':form})
def ordine(request):
    if request.method=='POST':
        formm = OrdineForm(request.POST , request.FILES)

        if formm.is_valid():
            myform = formm.save(commit=False)
            myform.ordini = request.ord
            myform.save


            return redirect(reverse('ordine'))

    else:
        form = PrenotaForm()

    return render(request,'ordine.html',{'form':form})
def prenotazione(request):
    return render(request,'prenotazione.html')

