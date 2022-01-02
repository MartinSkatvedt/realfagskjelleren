from rest_framework import serializers
from .models import Product, Merch, ProductCount, TotalProductCount

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image')


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = ('id', 'name', 'description', 'amount', 'price', 'image')

class ProductCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCount
        fields = ('id', 'date', 'amount', 'product')

class TotalProductCountSerializer(serializers.ModelSerializer):
    data = ProductCountSerializer(many=True)

    def create(self, validated_data):
        data = validated_data.pop('data')
        totalProductCount = TotalProductCount.objects.create(**validated_data)
        for item in data:
            item = ProductCount.objects.create(**item)
            totalProductCount.data.add(item)
        return totalProductCount
    
  
    class Meta:
        model = TotalProductCount
        fields = ('id', 'date', 'author', 'data')
