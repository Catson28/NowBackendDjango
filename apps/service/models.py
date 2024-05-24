from django.db import models

# Create your models here.
from django.db import models
from apps.subcategory.models import Subcategory
from apps.image.models import ServiceImage


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # este ee o preco base do servico
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, related_name="subcat_prod")
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Define um campo para a taxa horária do serviço.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FinancialAnalysis(models.Model):
    cost = models.FloatField(max_length=100)  # (Unidade de Producao) quantidade de produtos usados, ou usuabilidaade por servico
    #   o consumo sera igual quantidade de
    liquid = models.DecimalField(max_digits=10, decimal_places=2) #   liquid  este ee o lucro liquido que resulta da subracao do preco negociado pelo custo dos produtos usados
    margin = models.DecimalField(max_digits=10, decimal_places=2) #   margin ee a margem de lucro resulta do preco base pelos custos de produtos
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE)
    business = models.DecimalField(max_digits=10, decimal_places=2) #   este ee o preco negociado com o cliente
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# isto sera feito em outra tabela
#   este ee o lucro operacional resulta da subracao do lucro liquido por custos fixos
    #   este ee o preco negociado com o cliente
