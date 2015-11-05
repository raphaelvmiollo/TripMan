#coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login, logout # funcoes que salvam e liberam o usuario na sessao
from django.contrib.auth.decorators import login_required
from models import *
from forms import *
from django.contrib import auth
from django.contrib.auth.hashers import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your views here.


def indexAdmin(request):
    return render(request, "indexAdmin.html")    
	
def indexDriver(request):
    return render(request, "indexDriver.html")    

def indexClient(request):
    return render(request, "indexClient.html")    

def viewPassengers(request, tid):
    via = Viagem.objects.get(pk=tid)
    passageiros = via.passageiros.all()
    
    total, capacidade = (len(passageiros),via.veiculo.numAssentos)
    
    if request.method == "POST":
      form = ManPassageiroForm(request.POST)
      if form.is_valid():
	nome = form.cleaned_data['nome']
	matricula_siape = form.cleaned_data['matricula_siape']
	cargoUsuario = form.cleaned_data['cargoUsuario']
	identidade = form.cleaned_data['identidade']
	
	#p = Passageiro.objects.get(matricula_siape = matricula_siape)
	p = (Passageiro.objects.filter(matricula_siape = matricula_siape) or [None])[0]
	
	if p is None:
	  p = Passageiro.objects.create(nome = nome, matricula_siape = matricula_siape, cargoUsuario = cargoUsuario, identidade = identidade)
	  p.save()
	  
	v = Viagem.objects.get(pk=tid)
	v.passageiros.add(p)
      else:
	return render(request, "viewPassengers.html", {"form" : form, "title" : "Passageiros ", "total":total, "capacidade":capacidade, 'passageiros' : passageiros, 'trid' : via.id})
    return render(request, "viewPassengers.html", {"form" : ManPassageiroForm(), 'passageiros' : passageiros, 'trid' : via.id, "title" : "Passageiros ", "total":total, "capacidade":capacidade})
    
def removePassenger(request, tid, pid):
    v = Viagem.objects.get(pk=tid)
    p = Passageiro.objects.get(pk=pid)
    v.passageiros.remove(p)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def subIndexUsers(request):
    users = Usuario.objects.all()
    howManyAdmins = Usuario.objects.filter(tipoUsuario = 1) # Search for all adminstrators
    if len(howManyAdmins) == 1:
      howManyAdmins = True
    else:
      howManyAdmins = False
    return render(request, "subIndexUsers.html", {'users' : users, 'uniqueAdm' : howManyAdmins}) 

def addUser(request):
    if request.method == "POST":
      if 'voltar' in request.POST:
	return HttpResponseRedirect("/subIndexUsers")      
      form = AddUserForm(request.POST)
      if form.is_valid():
	nome = form.cleaned_data['nome_usuario']
	username = form.cleaned_data['username']
	mat = form.cleaned_data['matricula_siape']
	senha = form.cleaned_data['senha']
	email = form.cleaned_data['email']
	cargoUsuario = form.cleaned_data['cargoUsuario']
	tipoUsuario = form.cleaned_data['tipoUsuario']
	userexi = User.objects.filter(username = username)
	usuarioexi = Usuario.objects.filter(matricula_siape = mat)
	if len(userexi) ==0  and len(usuarioexi)==0:
	  user = User.objects.create_user(username = username, first_name = nome[:nome.find(' ')], last_name = nome[nome.find(' ')+1:], email = email, password = senha)    
	  usuario = Usuario.objects.create(usuario = user, matricula_siape = mat, cargoUsuario = cargoUsuario, tipoUsuario = tipoUsuario)
	  user.save()
	  usuario.save()
	elif len(userexi) > 0:
	  messages.warning(request, u'O nome de usuário já está cadastrado no sistema!')
	  return render(request, "addUser.html", {"form":form,  "title" : "Cadastrar usuário", "nomebotao":"Cadastrar"})
	elif len(usuarioexi) > 0:
	  messages.warning(request, u'A matrícula ou SIAPE já está cadastrada no sistema!')
	  return render(request, "addUser.html", {"form":form,  "title" : "Cadastrar usuário", "nomebotao":"Cadastrar"})
	return HttpResponseRedirect("subIndexUsers")
      else:
	return render(request, "addUser.html", {"form" : form, "title" : "Cadastrar usuário", "nomebotao":"Cadastrar"})
    return render(request, "addUser.html", {"form" : AddUserForm(), "title" : "Cadastrar usuário", "nomebotao":"Cadastrar"})

  
def editUser(request, uid):
    usuario = Usuario.objects.get(pk=uid)
    user = User.objects.get(pk=usuario.usuario.id)
    if request.method == "POST":
      if 'voltar' in request.POST:
	return HttpResponseRedirect("/subIndexUsers")      
      form = AddUserForm(request.POST)
      if form.is_valid():
	nome = form.cleaned_data['nome_usuario']
	username = form.cleaned_data['username']
	mat = form.cleaned_data['matricula_siape']
	senha = form.cleaned_data['senha']
	email = form.cleaned_data['email']
	cargoUsuario = form.cleaned_data['cargoUsuario']
	tipoUsuario = form.cleaned_data['tipoUsuario']
	
	userexi = []
	usuarioexi = []

	if user.username != username:
		userexi = User.objects.filter(username = username)

	if usuario.matricula_siape != mat:
		usuarioexi = Usuario.objects.filter(matricula_siape = mat)
	
	if len(userexi) ==0  and len(usuarioexi)==0:
	  uid1 = Usuario.objects.get(pk=uid).usuario.id
	  user2 = User.objects.get(pk=uid1)
	  user2.username = username
	  user2.first_name = nome[:nome.find(' ')]
	  user2.last_name = nome[nome.find(' ')+1:]
	  user2.email = email
	  user2.password = make_password(senha)
	  user2.save()
	  usuario = Usuario.objects.get(pk=uid)
	  usuario.usuario = user2
	  usuario.matricula_siape = mat
	  usuario.cargoUsuario = cargoUsuario
	  usuario.tipoUsuario = tipoUsuario
	  usuario.save()
	elif len(userexi) > 0:
	  messages.warning(request, u'O nome de usuário já está cadastrado no sistema!')
	  return render(request, "addUser.html", {"form":form,  "title" : "Editar usuário", "nomebotao":"Salvar"})
	elif len(usuarioexi) > 0:
	  messages.warning(request, u'A matrícula ou SIAPE já está cadastrada no sistema!')
	  return render(request, "addUser.html", {"form":form,  "title" : "Editar usuário", "nomebotao":"Salvar"})
	return HttpResponseRedirect("/subIndexUsers")
      else:
	return render(request, "addUser.html", {"form" : form, "title" : "Editar usuário", "nomebotao":"Salvar"})
    return render(request, "addUser.html", {"form" : AddUserForm(initial={"nome_usuario" : user.first_name+' '+user.last_name, "username" : user.username, "matricula_siape" : usuario.matricula_siape, "senha" : user.password, "email" : user.email, "cargoUsuario" : usuario.cargoUsuario, "tipoUsuario" : usuario.tipoUsuario}), "title" : "Editar usuário", "nomebotao":"Salvar"})
  
def removeUser(request, uid):
  u = Usuario.objects.get(pk=uid)

  retiduser = u.usuario.id
  infiduser = request.user.id

  User.objects.get(pk=u.usuario.id).delete()
  u.delete()

  if infiduser == retiduser:
    return signout(request)
  return HttpResponseRedirect("/subIndexUsers")
	

def subIndexTravels(request):
    travels = Viagem.objects.all()    
    
    for i in range(len(travels)):
      if travels[i].status == 'd' and travels[i].datahora_chegada < timezone.now():
	travels[i].status = 'k'
	travels[i].save()
    
    return render(request, "subIndexTravels.html", {'travels':travels})    

def subIndexReports(request):
    travels = Viagem.objects.filter(relatorio__isnull = False)    
    return render(request, "subIndexReports.html", {'travels':travels})    
  
def subIndexVehicles(request):
    v = Veiculo.objects.all()
    print(v)
    return render(request, "subIndexVehicles.html", {'vehicles':v})    

def viewReport(request, tid):
    viagem = Viagem.objects.get(pk=tid)
    return render(request, "viewReport.html", {'form': ViewReport(initial={ 'datahora_chegada':viagem.datahora_chegada,'datahora_saida':viagem.datahora_saida,'localidade_chegada':viagem.localidade_chegada,'localidade_saida':viagem.localidade_saida,'objetivo':viagem.objetivo,'observacoes':viagem.observacoes,'despesa_responsavel':viagem.despesa_responsavel, 'ramal_contato':viagem.ramal_contato, 'solicitante':viagem.solicitante, 'motorista':viagem.motorista, 'justificativa':viagem.justificativa, 'veiculo':viagem.veiculo, 'relatorio':viagem.relatorio})})


def viewReportedReport(request, tid):
    viagem = Viagem.objects.get(pk=tid)
    return render(request, "viewReportedReport.html", {'form': ViewReport(initial={ 'datahora_chegada':viagem.datahora_chegada,'datahora_saida':viagem.datahora_saida,'localidade_chegada':viagem.localidade_chegada,'localidade_saida':viagem.localidade_saida,'objetivo':viagem.objetivo,'observacoes':viagem.observacoes,'despesa_responsavel':viagem.despesa_responsavel, 'ramal_contato':viagem.ramal_contato, 'solicitante':viagem.solicitante, 'motorista':viagem.motorista, 'justificativa':viagem.justificativa, 'veiculo':viagem.veiculo, 'relatorio':viagem.relatorio})})
  
  
def addVehicle(request):
    if request.method == "POST":
      if 'voltar' in request.POST:
	return HttpResponseRedirect("/subIndexVehicles")      
      form = AddVehicleForm(request.POST)
      if form.is_valid():
	placa = form.cleaned_data['placa']
	marca = form.cleaned_data['marca']
	banheiro = form.cleaned_data['banheiro']
	potencia = form.cleaned_data['potencia']
	ano = form.cleaned_data['ano'].year
	manutencao = form.cleaned_data['manutencao']
	TipoVeiculo = form.cleaned_data['TipoVeiculo']
	numAssentos = form.cleaned_data['numAssentos']

	plaexi = Veiculo.objects.filter(placa = placa)
	
	if len(plaexi) ==0:
	  veh = Veiculo.objects.create(placa=placa,marca=marca,banheiro=banheiro,potencia=potencia,ano=ano,manutencao=manutencao,TipoVeiculo=TipoVeiculo, numAssentos=numAssentos)   
	  veh.save()
	elif len(plaexi) > 0:
	  messages.warning(request, u'A placa informada já está cadastrado no sistema!')
	  return render(request, "addVehicle.html", {"form":form,  "title" : "Cadastrar veículo", "nomebotao":"Cadastrar"})
	return HttpResponseRedirect("/subIndexVehicles")
      else:
	return render(request, "addVehicle.html", {"form" : form, "title" : "Cadastrar veículo", "nomebotao":"Cadastrar"})
    return render(request, "addVehicle.html", {"form" : AddVehicleForm(), "title" : "Cadastrar veículo", "nomebotao":"Cadastrar"})
    

  
def editVehicle(request, vid):
    vehicle = Veiculo.objects.get(pk=vid)
    if request.method == "POST":
      if 'voltar' in request.POST:
	return HttpResponseRedirect("/subIndexVehicles")      
      form = AddVehicleForm(request.POST)
      if form.is_valid():
	placa = form.cleaned_data['placa']
	marca = form.cleaned_data['marca']
	banheiro = form.cleaned_data['banheiro']
	potencia = form.cleaned_data['potencia']
	ano = form.cleaned_data['ano'].year
	manutencao = form.cleaned_data['manutencao']
	TipoVeiculo = form.cleaned_data['TipoVeiculo']
	numAssentos = form.cleaned_data['numAssentos']
	
	plaexi = []
	
	if placa != vehicle.placa:
	  plaexi = Veiculo.objects.filter(placa = placa)
	
	if len(plaexi) ==0:
	  vehicle.placa=placa
	  vehicle.marca=marca
	  vehicle.banheiro=banheiro
	  vehicle.potencia=potencia
	  vehicle.ano=ano
	  vehicle.manutencao=manutencao
	  vehicle.TipoVeiculo=TipoVeiculo
	  vehicle.numAssentos=numAssentos
	  vehicle.save()
	elif len(plaexi) > 0:
	  messages.warning(request, u'A placa informada já está cadastrado no sistema!')
	  return render(request, "addVehicle.html", {"form":form,  "title" : "Editar veículo", "nomebotao":"Editar"})
	return HttpResponseRedirect("/subIndexVehicles")
      else:
	return render(request, "addVehicle.html", {"form" : form, "title" : "Editar veículo", "nomebotao":"Editar"})
    return render(request, "addVehicle.html", {"form"
      :AddVehicleForm(initial={'placa':vehicle.placa,'marca':vehicle.marca,'banheiro':vehicle.banheiro,'potencia':vehicle.potencia,'ano':vehicle.ano,'manutencao':vehicle.manutencao,'TipoVeiculo':vehicle.TipoVeiculo, 'numAssentos':vehicle.numAssentos}), "title" : "Editar veículo", "nomebotao":"Editar"})
  
  
  
def removeVehicle(request, vid):
  u = Veiculo.objects.get(pk=vid)
  u.delete()
  return HttpResponseRedirect("/subIndexVehicles")
  pass








def addTravel(request):
    if request.method == "POST":
      if 'voltar' in request.POST:
	return HttpResponseRedirect("/subIndexTravels")      
      form = AddTravelForm(request.POST)
      if form.is_valid():
	datahora_saida = form.cleaned_data['datahora_saida']
	datahora_chegada = form.cleaned_data['datahora_chegada']
	localidade_saida = form.cleaned_data['localidade_saida']
	localidade_chegada = form.cleaned_data['localidade_chegada']
	objetivo = form.cleaned_data['objetivo']
	observacoes = form.cleaned_data['observacoes']
	despesa_responsavel = form.cleaned_data['despesa_responsavel']
	ramal_contato = form.cleaned_data['ramal_contato']
	veiculo = form.cleaned_data['veiculo']

	
        solicitante = Usuario.objects.get(usuario = request.user)
        
        motorista = None
        aprovador = None 
        status = 'n'

	via = Viagem.objects.create(datahora_saida=datahora_saida,datahora_chegada=datahora_chegada,localidade_saida=localidade_saida,localidade_chegada=localidade_chegada,objetivo=objetivo,observacoes=observacoes,despesa_responsavel=despesa_responsavel, ramal_contato=ramal_contato,veiculo=veiculo,   solicitante = solicitante, motorista = motorista, aprovador = aprovador, status = status)   
	via.save()
	
	return HttpResponseRedirect("/subIndexTravels")
      else:
	return render(request, "addTravel.html", {"form" : form, "title" : "Cadastrar Viagem", "nomebotao":"Cadastrar"})
    return render(request, "addTravel.html", {"form" : AddTravelForm(), "title" : "Cadastrar Viagem", "nomebotao":"Cadastrar"})


def approveTravel(request, tid):
    viagem = Viagem.objects.get(pk=tid)
    if request.method == "POST":
      if 'voltar' in request.POST:
	return HttpResponseRedirect("/subIndexTravels")      
      form = AppRejTravelForm(request.POST)
      if form.is_valid():
	motorista = form.cleaned_data['motorista']
	veiculo = form.cleaned_data['veiculo']
	status = form.cleaned_data['status']
	justificativa = form.cleaned_data['justificativa']
	
	statusToSave = 'i'	
	if status == True:
	  statusToSave = 'd'
	  
	viagem.status = statusToSave
	viagem.veiculo = veiculo
	viagem.justificativa = justificativa
	viagem.motorista = motorista
	viagem.aprovador = Usuario.objects.get(usuario = request.user)
	viagem.save()
	
	return HttpResponseRedirect("/subIndexTravels")
      else:
	return render(request, "approveTravel.html", {"form" : form, "title" : "Avaliar viagem", "nomebotao":"Avaliar"})
    status = viagem.status
    if status == 'd':
      status = True
    elif status == 'i':
      status = False
    return render(request, "approveTravel.html", {"form"
      :AppRejTravelForm(initial={ 'datahora_chegada':viagem.datahora_chegada,'datahora_saida':viagem.datahora_saida,'localidade_chegada':viagem.localidade_chegada,'localidade_saida':viagem.localidade_saida,'objetivo':viagem.objetivo,'observacoes':viagem.observacoes,'despesa_responsavel':viagem.despesa_responsavel, 'ramal_contato':viagem.ramal_contato, 'solicitante':viagem.solicitante, 'motorista':viagem.motorista, 'status':status, 'justificativa':viagem.justificativa, 'veiculo':viagem.veiculo}), "title" : "Avaliar viagem", "nomebotao":"Avaliar"} )




def removeTravel(request, tid):
  u = Viagem.objects.get(pk=tid)
  #u.delete()
  u.status='c'
  u.save()
  return HttpResponseRedirect("/subIndexTravels")
  pass

def viewTravel(request, tid):
   viagem = Viagem.objects.get(pk=tid)
   status = viagem.status
   if status == 'd':
      status = True
   elif status == 'i':
      status = False
   return render(request, "viewTravel.html", {"form"
      :ViewTravelForm(initial={ 'datahora_chegada':viagem.datahora_chegada,'datahora_saida':viagem.datahora_saida,'localidade_chegada':viagem.localidade_chegada,'localidade_saida':viagem.localidade_saida,'objetivo':viagem.objetivo,'observacoes':viagem.observacoes,'despesa_responsavel':viagem.despesa_responsavel, 'ramal_contato':viagem.ramal_contato, 'solicitante':viagem.solicitante, 'motorista':viagem.motorista, 'status':status, 'justificativa':viagem.justificativa, 'veiculo':viagem.veiculo}), "title" : "Visualizar viagem"} )

def submitReport(request, tid):
   viagem = Viagem.objects.get(pk=tid)
   if request.method == 'POST':
     form = ViewReport(request.POST)
     if form.is_valid():
       relatorio = form.cleaned_data['relatorio']
       viagem.relatorio = relatorio
       viagem.save()
       return HttpResponseRedirect("/subIndexDriverTravels")
   return render(request, "submitReport.html", {"form"
      :SubmitReport(initial={ 'datahora_chegada':viagem.datahora_chegada,'datahora_saida':viagem.datahora_saida,'localidade_chegada':viagem.localidade_chegada,'localidade_saida':viagem.localidade_saida,'objetivo':viagem.objetivo,'observacoes':viagem.observacoes,'despesa_responsavel':viagem.despesa_responsavel, 'ramal_contato':viagem.ramal_contato, 'solicitante':viagem.solicitante, 'motorista':viagem.motorista, 'justificativa':viagem.justificativa, 'veiculo':viagem.veiculo, 'relatorio':viagem.relatorio}), "title" : "Preencher relatório", 'nomebotao':'Salvar'} )

def addGuestUser(request):
    if request.method == "POST":
      if 'voltar' in request.POST:
	return HttpResponseRedirect("/")      
      form = AddGuestUserForm(request.POST)
      if form.is_valid():
	nome = form.cleaned_data['nome_usuario']
	username = form.cleaned_data['username']
	mat = form.cleaned_data['matricula_siape']
	senha = form.cleaned_data['senha']
	email = form.cleaned_data['email']
	cargoUsuario = form.cleaned_data['cargoUsuario']
	tipoUsuario = TipoUsuario.objects.get(descricao='Cliente')
	userexi = User.objects.filter(username = username)
	usuarioexi = Usuario.objects.filter(matricula_siape = mat)
	if len(userexi) ==0  and len(usuarioexi)==0:
	  user = User.objects.create_user(username = username, first_name = nome[:nome.find(' ')], last_name = nome[nome.find(' ')+1:], email = email, password = senha)    
	  usuario = Usuario.objects.create(usuario = user, matricula_siape = mat, cargoUsuario = cargoUsuario, tipoUsuario = tipoUsuario)
	  user.save()
	  usuario.save()
	elif len(userexi) > 0:
	  messages.warning(request, u'O nome de usuário já está cadastrado no sistema!')
	  return render(request, "addGuestUser.html", {"form":form,  "title" : "Cadastrar usuário", "nomebotao":"Cadastrar"})
	elif len(usuarioexi) > 0:
	  messages.warning(request, u'A matrícula ou SIAPE já está cadastrada no sistema!')
	  return render(request, "addGuestUser.html", {"form":form,  "title" : "Cadastrar usuário", "nomebotao":"Cadastrar"})
	return HttpResponseRedirect("/")
      else:
	return render(request, "addGuestUser.html", {"form" : form, "title" : "Cadastrar usuário", "nomebotao":"Cadastrar"})
    return render(request, "addGuestUser.html", {"form" : AddGuestUserForm(), "title" : "Cadastrar usuário", "nomebotao":"Cadastrar"})


def redirectUser(request):
    u = Usuario.objects.get(usuario = request.user) # usuario associado ao user logado
    if u.tipoUsuario.descricao == 'Administrador': # adminstrador
      return HttpResponseRedirect("indexAdmin") # redireciona o usuario logado para a pagina inicial
    elif u.tipoUsuario.descricao == 'Motorista': # motorista 
      return HttpResponseRedirect("indexDriver") # redireciona o usuario logado para a pagina inicial
    elif u.tipoUsuario.descricao == 'Cliente': # cliente
      return HttpResponseRedirect("indexClient") # redireciona o usuario logado para a pagina inicial


def index(request):
    
    if request.user is not None:
      print 'oi'
    viagem = Viagem.objects.all()
    print viagem
      
    from forms import CustomAuthenticationForm
    if request.method == 'POST':
      
         form = CustomAuthenticationForm(data=request.POST) 
         
         if "entrar" in request.POST:	
	   if form.is_valid():
              #se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados  
              curUser = form.get_user()
	      login(request, curUser)
	      u = Usuario.objects.get(usuario = curUser) # usuario associado ao user logado
	      #print(u.tipoUsuario)
	      if u.tipoUsuario.descricao == 'Administrador': # adminstrador
		return HttpResponseRedirect("indexAdmin") # redireciona o usuario logado para a pagina inicial
	      elif u.tipoUsuario.descricao == 'Motorista': # motorista 
		return HttpResponseRedirect("indexDriver") # redireciona o usuario logado para a pagina inicial
	      elif u.tipoUsuario.descricao == 'Cliente': # cliente
		return HttpResponseRedirect("indexClient") # redireciona o usuario logado para a pagina inicial
	   else:
	     return render(request, "index.html", {"form": form})
	   
         else:
	   return HttpResponseRedirect("addGuestUser")
	  
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, "index.html", {"form": CustomAuthenticationForm(), "viagem": viagem})

def editDriver(request):
    user = request.user
    if request.method == "POST":
      if 'voltar' in request.POST:
	return HttpResponseRedirect("/indexDriver")      
      form = EditUserForm(request.POST)
      if form.is_valid():
	nome = form.cleaned_data['nome_usuario']
	senha = form.cleaned_data['senha']
	email = form.cleaned_data['email']

	#uid = request.user.id
	#user2 = User.objects.get(pk=uid)
	user.first_name = nome[:nome.find(' ')]
	user.last_name = nome[nome.find(' ')+1:]
	user.email = email
	user.set_password(senha)
	user.save()
	if hasattr(auth, 'update_session_auth_hash'):
	  auth.update_session_auth_hash(request,user)
	#login(request,user2)
	
	return HttpResponseRedirect("/indexDriver")
      else:
	return render(request, "editUser.html", {"form" : form, "title" : "Editar usuário", "nomebotao":"Salvar"})
    return render(request, "editUser.html", {"form" : EditUserForm(initial={"nome_usuario" : user.first_name+' '+user.last_name, "username" : user.username, "senha" : user.password, "email" : user.email}), "title" : "Editar usuário", "nomebotao":"Salvar"})

def subIndexDriverTravels(request):
    usuario1 = Usuario.objects.get(usuario = request.user)
    travels = Viagem.objects.filter(motorista = usuario1)
    for i in range(len(travels)):
      if travels[i].status == 'd' and travels[i].datahora_chegada < timezone.now():
	travels[i].status = 'k'
	travels[i].save()
    return render(request, "subIndexDriverTravels.html", {'travels':travels})  

def signout(request):
  logout(request)
  return (HttpResponseRedirect("/"))