from rest_framework import serializers

from .models import Product, Recipe, RecipeProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'times_cooked')


class RecipeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeProduct
        fields = ('id', 'recipe', 'product', 'weight_in_grams')


class RecipeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'products')


class AddProductToRecipeSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    weight = serializers.IntegerField()

