from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "name",
            "territory_name",
            "dept_name",
            "itm_clr",
            "option_key",
            "price",
            "c1_price"



        )