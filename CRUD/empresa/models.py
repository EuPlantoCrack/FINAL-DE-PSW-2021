from django.db import models

# Create your models here.

class empresa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefone = models.CharField(max_length=10)
    departamento = models.CharField(max_length=17)

    def __str__(self):
        return self.nome 