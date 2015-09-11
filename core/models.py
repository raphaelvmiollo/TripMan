from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 

class Usuario(models.Model):
	usuario = models.ForeignKey(User) #Classe Usuario associas a cada "Usuario" um User do sistema de autenticacao
	matricula_siape = models.CharField(max_length = 20)
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


	



class Veiculo(models.Model):
 	placa = models.CharField(max_length=8)
 	marca = models.CharField(max_length=30)
 	banheiro = models.BooleanField()
 	potencia = models.IntegerField()
 	ano = models.IntegerField()
 	manutencao = models.BooleanField()
 	TipoVeiculo = models.ForeignKey('TipoVeiculo')


class TipoVeiculo(models.Model):
	descricao = models.CharField(max_length=30)
	qtdLugares = models.IntegerField()


