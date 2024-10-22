from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(default="Sem descrição")
    category = models.CharField(max_length=100, default="Geral")
    stock = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
