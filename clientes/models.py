from django.db import models


class Documentos(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
         return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=100,  decimal_places=4)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photo', null=True, blank=True)
    doc = models.OneToOneField(Documentos, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Produto(models.Model):
    descricão = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=4)

    def __str__(self):
        return self.descricão


class Venda(models.Model):
    numero = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=10,  decimal_places=4)
    desconto = models.DecimalField(max_digits=10,  decimal_places=4)
    imposto = models.DecimalField(max_digits=10,  decimal_places=4)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.numero
