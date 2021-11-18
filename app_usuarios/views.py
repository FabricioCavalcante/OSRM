from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
def cadastro(request):
    nome = request.POST['nome']
    email = request.POST['email']
    senha = request.POST['senha']
    senha2 = request.POST['senha2']
    if User.objects.filter(email=email).exists():
        return render(request, 'usuarios/cadastro.html')
    user = User.objects.create_user(username=nome, email=email, password=senha)
    user.save()
    return render(request, 'usuarios/login.html')
        
        
   # else:    
       # return render(request, 'usuarios/cadastro.html')

def login(request):
    pass

def logout(request):
    pass

def dashboard(request):
    pass