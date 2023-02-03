from django.db import models


class Deal(models.Model):
    customer = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()
