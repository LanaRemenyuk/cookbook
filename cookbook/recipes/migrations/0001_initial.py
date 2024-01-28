# Generated by Django 5.0.1 on 2024-01-26 17:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Продукт')),
                ('times_cooked', models.PositiveIntegerField(default=0, verbose_name='Количество раз использования в рецептах')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор рецепта')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_in_grams', models.PositiveIntegerField(verbose_name='Вес продукта в граммах')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_contained', to='recipes.product', verbose_name='Продукт')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_contained', to='recipes.recipe', verbose_name='Рецепт')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(related_name='products', through='recipes.RecipeProduct', to='recipes.product', verbose_name='Продукты'),
        ),
    ]