from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 

class Usuario(models.Model):
	usuario = models.ForeignKey(User) #Classe Usuario associas a cada "Usuario" um User do sistema de autenticacao
	matricula_siape = models.CharField(max_length = 20)
	senha = models.CharField(max_length = 45)
	#login = models.CharField(max_length = 20)
	#email = models.EmailField(max_length = 254)
	cargoUsuario =  models.ForeignKey('CargoUsuario')
	tipoUsuario = models.ForeignKey('TipoUsuario')

	def __str__(self):
		return self.usuario.username



class TipoUsuario(models.Model):
	descricao = models.CharField(max_length=30)

	def __str__(self):
		return self.descricao



class CargoUsuario(models.Model):
	descricao = models.CharField(max_length=30)

	def __str__(self):
		return self.descricao



class Localidade(models.Model):
	nome = models.CharField(max_length=254)
	latitude = models.CharField(max_length=254, default='')
	longitude = models.CharField(max_length=254, default='')
	
	def __str__(self):
		 return self.nome
	
	

class Veiculo(models.Model):
 	placa = models.CharField(max_length=8)
 	marca = models.CharField(max_length=30)
 	banheiro = models.BooleanField()
 	potencia = models.IntegerField()
 	ano = models.IntegerField()
 	manutencao = models.BooleanField()
 	TipoVeiculo = models.ForeignKey('TipoVeiculo')

	def __str__(self):
		 return self.marca + ' ' + self.placa



class TipoVeiculo(models.Model):
	descricao = models.CharField(max_length=30)
	qtdLugares = models.IntegerField()

	def __str__(self):
		 return self.descricao



class Passageiro(models.Model):
	nome = models.CharField(max_length=50)
	matricula_siape = models.CharField(max_length = 20)
	identidade = models.CharField(max_length = 20)
	cargoUsuario =  models.ForeignKey('CargoUsuario')
	
	def __str__(self):
		return self.nome
  
  
  
class Viagem(models.Model):
        datahora_saida = models.DateTimeField()
        datahora_chegada = models.DateTimeField()
        localidade_saida = models.ForeignKey('Localidade', related_name='saida', default='')
        localidade_chegada = models.ForeignKey('Localidade', related_name='chegada', default='')
        objetivo = models.TextField()
        observacoes = models.TextField()
        despesa_responsavel = models.CharField(max_length = 50)
        ramal_contato = models.IntegerField()
        veiculo = models.ForeignKey('Veiculo', default='')
        solicitante = models.ForeignKey('Usuario', related_name='solicitante', default='')
        motorista = models.ForeignKey('Usuario', related_name='motorista', default='')
        aprovador = models.ForeignKey('Usuario', related_name='aprovador', default='')
        passageiros = models.ManyToManyField('Passageiro', null=True)
        status = models.BooleanField()
  
        def __str__(self):
		return self.localidade_saida.nome + ' -> ' + self.localidade_chegada.nome
  
  
  
  