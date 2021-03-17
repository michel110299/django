from django.db import models

class Categoria (models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Transacoes(models.Model):
    Data = models.DateTimeField()
    Descricao = models.CharField(max_length=200)
    Valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    observacoes = models.TextField('Observações transações',null=True, blank=True)

    def __str__(self):
        return self.Descricao



    