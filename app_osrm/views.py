from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from app_osrm.models import InserirDados
from app_osrm.forms import ListaForm
import datetime
# Create your views here.
def home(request):
    return render(request, 'index.html')

def lista(request):
    data = {}
    data['db'] = InserirDados.objects.all()
    return render(request, 'lista.html', data)

def form(request):
    data = {}
    data['form'] = ListaForm()
    return render(request, 'form.html', data)

def create(request):
    form = ListaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = InserirDados.objects.get(pk=pk)
    return render(request, 'view.html',data)