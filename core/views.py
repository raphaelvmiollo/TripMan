from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login # funcao que salva o usuario na sessao
from django.contrib.auth.decorators import login_required
from models import *

# Create your views here.


def indexADM(request):
    return render(request, "indexAdministrador.html")    
	
	
def logar(request):
    from forms import CustomAuthenticationForm
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST) 
        
        if form.is_valid():
            #se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
          
            login(request, form.get_user())
            return HttpResponseRedirect("indexadmin") # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, "login.html", {"form": form})
    
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, "login.html", {"form": CustomAuthenticationForm()})
				