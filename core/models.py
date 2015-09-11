from django.db import models

# Create your models here.
 
class Localidade(models.Model):
	nome = models.CharField(max_length = 60)
	latitude = models.CharField(max_length = 20)
	longitude = models.CharField(max_length = 20)
	
	def __str__(self):
		return self.nome
	
class Viagem(models.Model):
	localidadeDestino = models.ForeignKey(Localidade)
	
	
	 