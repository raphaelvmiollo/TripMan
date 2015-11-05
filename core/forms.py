# -*- coding: utf-8 -*-

from models import *
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomAuthenticationForm(AuthenticationForm):

	def __init__(self, *args, **kwargs):
		super(CustomAuthenticationForm,self).__init__(*args,**kwargs)
		
		self.fields['username'].label =  u''#Usuário'
		self.fields['password'].label =  u''#Senha'

		self.fields['username'].widget.attrs['class']="form-control"
		self.fields['password'].widget.attrs['class']="form-control"

		self.fields['username'].widget.attrs['placeholder']=u'Usuário'
		self.fields['password'].widget.attrs['placeholder']=u'Senha'

		
class AddUserForm(forms.Form):
   
    nome_usuario = forms.CharField(label = 'Nome completo', max_length = 255, widget = forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label = 'Nome de usuário', max_length = 255 ,widget = forms.TextInput(attrs={'class': 'form-control'}) )
    matricula_siape = forms.CharField(label = 'Matrícula/SIAPE', max_length = 20 ,widget = forms.TextInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(label = 'Senha', max_length = 45, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label = 'E-mail', max_length = 254, widget = forms.TextInput(attrs={'class': 'form-control'}))
    cargoUsuario =  forms.ModelChoiceField(label = 'Cargo', queryset=CargoUsuario.objects.all(),widget = forms.Select(attrs={'class': 'form-control'}))
    tipoUsuario = forms.ModelChoiceField(label = 'Tipo', queryset=TipoUsuario.objects.all(), widget = forms.Select(attrs={'class': 'form-control'}))

class EditUserForm(forms.Form):
   
    nome_usuario = forms.CharField(label = 'Nome completo', max_length = 255, widget = forms.TextInput(attrs={'class': 'form-control'}))
    #username = forms.CharField(label = 'Nome de usuário', max_length = 255 ,widget = forms.TextInput(attrs={'class': 'form-control'}) )
    #matricula_siape = forms.CharField(label = 'Matrícula/SIAPE', max_length = 20 ,widget = forms.TextInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(label = 'Senha', max_length = 45, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label = 'E-mail', max_length = 254, widget = forms.TextInput(attrs={'class': 'form-control'}))
    #cargoUsuario =  forms.ModelChoiceField(label = 'Cargo', queryset=CargoUsuario.objects.all(),widget = forms.Select(attrs={'class': 'form-control'}))
    #tipoUsuario = forms.ModelChoiceField(label = 'Tipo', queryset=TipoUsuario.objects.all(), widget = forms.Select(attrs={'class': 'form-control'}))

class AddGuestUserForm(forms.Form):
   
    nome_usuario = forms.CharField(label = 'Nome completo', max_length = 255, widget = forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label = 'Nome de usuário', max_length = 255 ,widget = forms.TextInput(attrs={'class': 'form-control'}) )
    matricula_siape = forms.CharField(label = 'Matrícula/SIAPE', max_length = 20 ,widget = forms.TextInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(label = 'Senha', max_length = 45, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label = 'E-mail', max_length = 254, widget = forms.TextInput(attrs={'class': 'form-control'}))
    cargoUsuario =  forms.ModelChoiceField(label = 'Cargo', queryset=CargoUsuario.objects.all(),widget = forms.Select(attrs={'class': 'form-control'}))
    #tipoUsuario = forms.ModelChoiceField(label = 'Tipo', queryset=TipoUsuario.objects.all())


class AddVehicleForm(forms.Form):
  
    placa = forms.CharField(max_length=8, label = 'Placa', widget = forms.TextInput(attrs={'class': 'form-control'}))
    marca = forms.CharField(max_length=30, label = 'Marca', widget = forms.TextInput(attrs={'class': 'form-control'}))
    banheiro = forms.TypedChoiceField(label = 'Banheiro', coerce=lambda x: x == 'True',  choices=((False, 'Não'), (True, 'Sim')),  widget=forms.RadioSelect(attrs={'class': 'radio-inline'}))
    potencia = forms.IntegerField(label='Potência', widget = forms.TextInput(attrs={'class': 'form-control'}))
    #ano = forms.IntegerField(label='Ano de aquisição')
    ano = forms.DateField(label = 'Ano de aquisição', widget=forms.DateInput( format = '%Y' ,attrs={'class': 'form-control'}), input_formats=['%Y'])
    manutencao = forms.TypedChoiceField(label = 'Manutenção', coerce=lambda x: x == 'True',  choices=((False, 'Não'), (True, 'Sim')),  widget=forms.RadioSelect(attrs={'class': 'radio-inline'}))
    #TipoVeiculo = forms.ModelChoiceField(label = 'Tipo de Veículo', queryset=TipoVeiculo.objects.all(),widget = forms.Select(attrs={'class': 'form-control'}))
    TipoVeiculo = forms.CharField(max_length=30, label = 'Tipo de Veículo', widget = forms.TextInput(attrs={'class': 'form-control'}))
    numAssentos = forms.IntegerField(label='Número de Assentos', widget = forms.TextInput(attrs={'class': 'form-control'}))
    
    
class AddTravelForm(forms.Form):
  
    datahora_saida = forms.DateTimeField(label = 'Data/Horário de Partida',widget=forms.DateTimeInput(attrs={'class':'form-control'}, format = '%d/%m/%Y - %H:%M'), input_formats=['%d/%m/%Y - %H:%M'])
    datahora_chegada = forms.DateTimeField(label = 'Data/Horário de Chegada',widget=forms.DateTimeInput(attrs={'class':'form-control'}, format = '%d/%m/%Y - %H:%M'), input_formats=['%d/%m/%Y - %H:%M'])
    localidade_saida = forms.ModelChoiceField(label = 'Localidade de Partida',  queryset=Localidade.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    localidade_chegada = forms.ModelChoiceField(label = 'Localidade de Chegada',  queryset=Localidade.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    objetivo = forms.CharField(label = 'Objetivo', widget=forms.Textarea(attrs={'class':'form-control'}))
    observacoes = forms.CharField(label = 'Observações',widget=forms.Textarea(attrs={'class':'form-control'}))
    despesa_responsavel = forms.CharField(label = 'Responsável pela Despesa',max_length = 50, widget=forms.TextInput(attrs={'class':'form-control'}))
    ramal_contato = forms.IntegerField(label = 'Ramal',widget=forms.TextInput(attrs={'class':'form-control'}))
    veiculo = forms.ModelChoiceField(label = 'Veiculo',  queryset=Veiculo.objects.filter(manutencao = False), widget=forms.Select(attrs={'class':'form-control'}))
    

class AppRejTravelForm(AddTravelForm):
    
    datahora_saida = forms.DateTimeField(label = 'Data/Horário de Partida',widget=forms.DateTimeInput(attrs={'class':'form-control', 'readonly':True}, format = '%d/%m/%Y - %H:%M'), input_formats=['%d/%m/%Y - %H:%M'])
    datahora_chegada = forms.DateTimeField(label = 'Data/Horário de Chegada',widget=forms.DateTimeInput(attrs={'class':'form-control', 'readonly':True}, format = '%d/%m/%Y - %H:%M'), input_formats=['%d/%m/%Y - %H:%M'])
    localidade_saida = forms.ModelChoiceField(label = 'Localidade de Partida',  queryset=Localidade.objects.all(), widget=forms.Select(attrs={'class':'form-control',  'readonly':True}))
    localidade_chegada = forms.ModelChoiceField(label = 'Localidade de Chegada',  queryset=Localidade.objects.all(), widget=forms.Select(attrs={'class':'form-control',  'readonly':True}))
    objetivo = forms.CharField(label = 'Objetivo', widget=forms.Textarea(attrs={'class':'form-control', 'readonly':True}))
    observacoes = forms.CharField(label = 'Observações',widget=forms.Textarea(attrs={'class':'form-control', 'readonly':True}))
    despesa_responsavel = forms.CharField(label = 'Responsável pela Despesa',max_length = 50, widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    ramal_contato = forms.IntegerField(label = 'Ramal',widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    
    veiculo = forms.ModelChoiceField(label = 'Veiculo',  queryset=Veiculo.objects.filter(manutencao = False), widget=forms.Select(attrs={'class':'form-control'}))   
   
    solicitante = forms.ModelChoiceField(label = 'Solicitante', widget=forms.Select(attrs={'class':'form-control',  'readonly':True}), queryset=Usuario.objects.all())
    
    motorista = forms.ModelChoiceField(label = 'Motorista', widget=forms.Select(attrs={'class':'form-control'}), queryset=Usuario.objects.filter(tipoUsuario = 2))
    #aprovador = forms.ModelChoiceField(label = 'Usuario',  widget=forms.Select(attrs={'class':'form-control'}))
    #passageiros = forms.ManyToManyField(label = 'Passageiro',  widget=forms.Select(attrs={'class':'form-control'}))
    status = forms.TypedChoiceField(coerce=lambda x: x == 'True',  choices=((False, 'Indeferir'), (True, 'Deferir')),  widget=forms.RadioSelect(attrs={'class': 'radio-inline'}))
    justificativa = forms.CharField(label = 'Justificativa', widget=forms.Textarea(attrs={'class':'form-control'}), required=False)
    

class ViewTravelForm(AddTravelForm):
    
    datahora_saida = forms.DateTimeField(label = 'Data/Horário de Partida',widget=forms.DateTimeInput(attrs={'class':'form-control', 'readonly':True}, format = '%d/%m/%Y - %H:%M'), input_formats=['%d/%m/%Y - %H:%M'])
    datahora_chegada = forms.DateTimeField(label = 'Data/Horário de Chegada',widget=forms.DateTimeInput(attrs={'class':'form-control', 'readonly':True}, format = '%d/%m/%Y - %H:%M'), input_formats=['%d/%m/%Y - %H:%M'])
    localidade_saida = forms.ModelChoiceField(label = 'Localidade de Partida',  queryset=Localidade.objects.all(), widget=forms.Select(attrs={'class':'form-control',  'readonly':True}))
    localidade_chegada = forms.ModelChoiceField(label = 'Localidade de Chegada',  queryset=Localidade.objects.all(), widget=forms.Select(attrs={'class':'form-control',  'readonly':True}))
    objetivo = forms.CharField(label = 'Objetivo', widget=forms.Textarea(attrs={'class':'form-control', 'readonly':True}))
    observacoes = forms.CharField(label = 'Observações',widget=forms.Textarea(attrs={'class':'form-control', 'readonly':True}))
    despesa_responsavel = forms.CharField(label = 'Responsável pela Despesa',max_length = 50, widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    ramal_contato = forms.IntegerField(label = 'Ramal',widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    
    veiculo = forms.ModelChoiceField(label = 'Veiculo',  queryset=Veiculo.objects.all(), widget=forms.Select(attrs={'class':'form-control', 'readonly':True}))   
   
    solicitante = forms.ModelChoiceField(label = 'Solicitante', widget=forms.Select(attrs={'class':'form-control',  'readonly':True}), queryset=Usuario.objects.all())
    
    motorista = forms.ModelChoiceField(label = 'Motorista', widget=forms.Select(attrs={'class':'form-control', 'readonly':True}), queryset=Usuario.objects.filter(tipoUsuario = 2))
    #aprovador = forms.ModelChoiceField(label = 'Usuario',  widget=forms.Select(attrs={'class':'form-control'}))
    #passageiros = forms.ManyToManyField(label = 'Passageiro',  widget=forms.Select(attrs={'class':'form-control'}))
    status = forms.TypedChoiceField(coerce=lambda x: x == 'True',  choices=((False, 'Indeferir'), (True, 'Deferir')),  widget=forms.RadioSelect(attrs={'class': 'radio-inline', 'readonly':True, 'disabled':True}))
    justificativa = forms.CharField(label = 'Justificativa', widget=forms.Textarea(attrs={'class':'form-control', 'readonly':True}), required=False)
    
class ManPassageiroForm(forms.Form):
	nome = forms.CharField(label = 'Nome', max_length=50)
	matricula_siape = forms.CharField(label = 'Matrícula / SIAPE', max_length = 20)
	identidade = forms.IntegerField(label = 'Identidade')
	cargoUsuario =  forms.ModelChoiceField(label = 'Cargo', widget=forms.Select(attrs={'class':'form-control'}), queryset=CargoUsuario.objects.all())
	
class ViewReport(AddTravelForm):
    
    datahora_saida = forms.DateTimeField(label = 'Data/Horário de Partida',widget=forms.DateTimeInput(attrs={'class':'form-control', 'readonly':True}, format = '%d/%m/%Y - %H:%M'), input_formats=['%d/%m/%Y - %H:%M'])
    datahora_chegada = forms.DateTimeField(label = 'Data/Horário de Chegada',widget=forms.DateTimeInput(attrs={'class':'form-control', 'readonly':True}, format = '%d/%m/%Y - %H:%M'), input_formats=['%d/%m/%Y - %H:%M'])
    localidade_saida = forms.ModelChoiceField(label = 'Localidade de Partida',  queryset=Localidade.objects.all(), widget=forms.Select(attrs={'class':'form-control',  'readonly':True}))
    localidade_chegada = forms.ModelChoiceField(label = 'Localidade de Chegada',  queryset=Localidade.objects.all(), widget=forms.Select(attrs={'class':'form-control',  'readonly':True}))
    objetivo = forms.CharField(label = 'Objetivo', widget=forms.Textarea(attrs={'class':'form-control', 'readonly':True}))
    observacoes = forms.CharField(label = 'Observações',widget=forms.Textarea(attrs={'class':'form-control', 'readonly':True}))
    despesa_responsavel = forms.CharField(label = 'Responsável pela Despesa',max_length = 50, widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    ramal_contato = forms.IntegerField(label = 'Ramal',widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    
    veiculo = forms.ModelChoiceField(label = 'Veiculo',  queryset=Veiculo.objects.all(), widget=forms.Select(attrs={'class':'form-control','readonly':True}))   
   
    solicitante = forms.ModelChoiceField(label = 'Solicitante', widget=forms.Select(attrs={'class':'form-control',  'readonly':True}), queryset=Usuario.objects.all())
    
    motorista = forms.ModelChoiceField(label = 'Motorista', widget=forms.Select(attrs={'class':'form-control',  'readonly':True}), queryset=Usuario.objects.filter(tipoUsuario = 2))
    #aprovador = forms.ModelChoiceField(label = 'Usuario',  widget=forms.Select(attrs={'class':'form-control'}))
    #passageiros = forms.ManyToManyField(label = 'Passageiro',  widget=forms.Select(attrs={'class':'form-control'}))
    justificativa = forms.CharField(label = 'Justificativa', widget=forms.Textarea(attrs={'class':'form-control','readonly':True}))
    relatorio = forms.CharField(label = 'Relatório', widget=forms.Textarea(attrs={'class':'form-control',  'readonly':True}))
    
    
class SubmitReport(AddTravelForm):
    
    datahora_saida = forms.DateTimeField(label = 'Data/Horário de Partida',widget=forms.DateTimeInput(attrs={'class':'form-control', 'readonly':True}, format = '%d/%m/%Y - %H:%M'), input_formats=['%d/%m/%Y - %H:%M'])
    datahora_chegada = forms.DateTimeField(label = 'Data/Horário de Chegada',widget=forms.DateTimeInput(attrs={'class':'form-control', 'readonly':True}, format = '%d/%m/%Y - %H:%M'), input_formats=['%d/%m/%Y - %H:%M'])
    localidade_saida = forms.ModelChoiceField(label = 'Localidade de Partida',  queryset=Localidade.objects.all(), widget=forms.Select(attrs={'class':'form-control',  'readonly':True}))
    localidade_chegada = forms.ModelChoiceField(label = 'Localidade de Chegada',  queryset=Localidade.objects.all(), widget=forms.Select(attrs={'class':'form-control',  'readonly':True}))
    objetivo = forms.CharField(label = 'Objetivo', widget=forms.Textarea(attrs={'class':'form-control', 'readonly':True}))
    observacoes = forms.CharField(label = 'Observações',widget=forms.Textarea(attrs={'class':'form-control', 'readonly':True}))
    despesa_responsavel = forms.CharField(label = 'Responsável pela Despesa',max_length = 50, widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    ramal_contato = forms.IntegerField(label = 'Ramal',widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    
    veiculo = forms.ModelChoiceField(label = 'Veiculo',  queryset=Veiculo.objects.all(), widget=forms.Select(attrs={'class':'form-control','readonly':True}))   
   
    solicitante = forms.ModelChoiceField(label = 'Solicitante', widget=forms.Select(attrs={'class':'form-control',  'readonly':True}), queryset=Usuario.objects.all())
    
    motorista = forms.ModelChoiceField(label = 'Motorista', widget=forms.Select(attrs={'class':'form-control',  'readonly':True}), queryset=Usuario.objects.filter(tipoUsuario = 2))
    #aprovador = forms.ModelChoiceField(label = 'Usuario',  widget=forms.Select(attrs={'class':'form-control'}))
    #passageiros = forms.ManyToManyField(label = 'Passageiro',  widget=forms.Select(attrs={'class':'form-control'}))
    justificativa = forms.CharField(label = 'Justificativa', widget=forms.Textarea(attrs={'class':'form-control','readonly':True}))
    relatorio = forms.CharField(label = 'Relatório', widget=forms.Textarea(attrs={'class':'form-control'}))