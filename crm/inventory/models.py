from django.db import models

# Create your models here.


class Inventory(models.Model):
    item = models.CharField(max_length=100)
    quantity_left = models.IntegerField()
    quantity_sold = models.IntegerField()
    price = models.FloatField()
    sales_details = models.IntegerField()


class Sales(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField()
    inventory_id = models.OneToOneField(Inventory, on_delete=models.CASCADE)



