from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login, logout # funcoes que salvam e liberam o usuario na sessao
from django.contrib.auth.decorators import login_required
from models import *

# Create your views here.


def indexAdmin(request):
    return render(request, "indexAdmin.html")    
	
def indexDriver(request):
    return render(request, "indexDriver.html")    

def indexClient(request):
    return render(request, "indexClient.html")    

def subIndexUsers(request):
    users = User.objects.all()
    return render(request, "subIndexUsers.html", {'users' : users})    
	
def subIndexTravels(request):
    return render(request, "subIndexTravels.html")    

def subIndexVehicles(request):
    return render(request, "subIndexVehicles.html")    

def signin(request):
    from forms import CustomAuthenticationForm
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST) 
        
        if form.is_valid():
            #se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
            
            curUser = form.get_user()
            
            login(request, curUser)
            
            if curUser.is_staff and curUser.is_superuser: # adminstrador
	      return HttpResponseRedirect("indexAdmin") # redireciona o usuario logado para a pagina inicial
	    elif curUser.is_staff: # motorista 
	      return HttpResponseRedirect("indexDriver") # redireciona o usuario logado para a pagina inicial
	    else: # cliente
	      return HttpResponseRedirect("indexClient") # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, "signin.html", {"form": form})
    
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, "signin.html", {"form": CustomAuthenticationForm()})

def signout(request):
  logout(request)
  return (HttpResponseRedirect("/"))