from django.contrib import admin

from .models import Product, Recipe, RecipeProduct

EMPTY_VALUE = '-пусто-'


class RecipeProductInLine(admin.TabularInline):
    """Представляет модель RecipeProduct в интерфейсе администратора."""
    model = RecipeProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Представляет модель Product в интерфейсе администратора."""
    list_display = ('id', 'name', 'times_cooked')
    search_fields = ('name',)
    list_filter = ('name',)
    #inlines = (RecipeProductInLine,)
    empty_value_display = EMPTY_VALUE


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Представляет модель Recipe в интерфейсе администратора."""
    list_display = ('id', 'name')
    search_fields = ('name',)
    inlines = (RecipeProductInLine,)
    empty_value_display = EMPTY_VALUE
