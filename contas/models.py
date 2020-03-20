from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Categorias"


class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacao = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Transações"
