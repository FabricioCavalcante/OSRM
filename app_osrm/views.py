from django.contrib.auth.models import User
from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from app_osrm.models import InserirDados, setor
from app_osrm.forms import ListaForm

def home(request):
    return render(request, 'index.html')

def lista(request):
    data = {}
    data['db'] = InserirDados.objects.all()
    return render(request, 'lista.html', data)

def form(request):
    if request.method == 'POST':
        placa_patrimonio = request.POST['placa_patrimonio']
        local = request.POST['local']
        problema = request.POST['problema']
        
        user = get_object_or_404(User, pk=request.user.id)
        
        requisicao = InserirDados.objects.create(nome=user, placa_patrimonio=placa_patrimonio, local=local, problema=problema)
        requisicao.save()
        return redirect('dashboard')
    else:
        return render(request, 'form.html')

def create(request):
    form = ListaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

def view(request, pk):
    data = {}
    data['db'] = InserirDados.objects.get(pk=pk)
    return render(request, 'view.html',data)

def criar_setor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        guardar_nome_setor = setor.objects.create(nome=nome)
        guardar_nome_setor.save()
    return render(request, 'setor.html')

def criar_tecnico(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        guardar_nome_setor = setor.objects.create(nome=nome)
        guardar_nome_setor.save()
    return render(request, 'setor.html')