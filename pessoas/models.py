from django.db import models

# Create your models here.



class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome