from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    territory_name = models.CharField(max_length=255)
    dept_name = models.CharField(max_length=255)
    itm_clr = models.CharField(max_length=255)
    option_key = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    c1_price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

