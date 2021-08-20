from django.db import models

class Productos(models.Model):
    cod_product = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=150)
    create = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=150)
    price= models.FloatField()
    stock = models.IntegerField()
    

    def __str__(self):
        return self.description

    

