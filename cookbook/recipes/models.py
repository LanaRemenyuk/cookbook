from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=200,
                            verbose_name='Продукт',
                            )
    times_cooked = models.PositiveIntegerField(default=0,
                                        verbose_name='Количество раз использования в рецептах'
                                               )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Recipe(models.Model):
    """Модель рецепта"""
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(to=Product,
                                      through='RecipeProduct',
                                      related_name='products',
                                      verbose_name='Продукты')

    def __str__(self):
        return self.name


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='product_contained',
        verbose_name='Рецепт')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_contained',
        verbose_name='Продукт')
    weight_in_grams = models.PositiveIntegerField(
        default=0,
        verbose_name='Вес продукта в граммах')

    def __str__(self):
        return f"{self.recipe} - {self.product} - {self.weight_in_grams} гр."

    class Meta:
        unique_together = ('recipe', 'product')