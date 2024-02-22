from django.db import models

class Coffee(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    quantity=models.IntegerField()
    image=models.CharField(max_length=2083)

