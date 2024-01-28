from collections import defaultdict

from django.db import transaction
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Product, Recipe, RecipeProduct
from .serializers import (ProductSerializer, RecipeProductSerializer,
                          RecipeSerializer)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RecipeProductViewSet(viewsets.ModelViewSet):
    queryset = RecipeProduct.objects.all()
    serializer_class = RecipeProductSerializer


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @transaction.atomic
    @action(detail=False, methods=['post'])
    def add_product_to_recipe(self, request, pk=None):
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')

        if not recipe_id or not product_id or not weight:
            return Response({'ошибка': 'Не все параметры переданы'}, status=400)

        try:
            recipe_product = RecipeProduct.objects.get(recipe_id=recipe_id, product_id=product_id)
            recipe_product.weight_in_grams = weight
            recipe_product.save()
        except RecipeProduct.DoesNotExist:
            RecipeProduct.objects.create(recipe_id=recipe_id, product_id=product_id, weight_in_grams=weight)

        return Response({'статус': 'Продукт успешно добавлен к рецепту', 'данные_о_продукте': {
            'id рецепта': recipe_id,
            'id продукта': product_id,
            'вес в граммах': weight
        }})

    @transaction.atomic
    @action(detail=False, methods=['post'])
    def cook_recipe(self, request):
        recipe_id = request.GET.get('recipe_id')

        if not recipe_id:
            return Response({'ошибка': 'Не передан идентификатор рецепта'}, status=400)

        try:
            recipe_products = RecipeProduct.objects.filter(recipe_id=recipe_id)
            products_usage = defaultdict(int)

            for recipe_product in recipe_products:
                product = recipe_product.product
                products_usage[product.name] += 1

            return Response({'статус': 'Рецепт успешно приготовлен',
                             'продукты из рецепта использованы столько раз': dict(products_usage)})
        except RecipeProduct.DoesNotExist:
            return Response({'ошибка': 'Рецепт не найден'}, status=404)

    @action(detail=False, methods=['get'])
    def show_recipes_without_product(self, request, pk=None):
        context = {}
        product_id = request.GET.get('product_id')
        template = 'recipes_without_prod.html'

        try:
            filtered_recipes = Recipe.objects.exclude(
                products__id=product_id,
                product_contained__weight_in_grams__gte=10
            )

            context['recipes'] = filtered_recipes

            return render(request, template, context)
        except Exception as e:
            return Response({'ошибка': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

