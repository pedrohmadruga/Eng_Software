from django.db import models

class UserCPF(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

class UserCNPJ(models.Model):
    cnpj = models.CharField(max_length=14, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(default="")
    password = models.CharField(max_length=20)