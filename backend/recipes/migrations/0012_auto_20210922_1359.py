# Generated by Django 3.0.5 on 2021-09-22 10:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20210922_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='amount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0, 'Количество должно быть положительным числом')], verbose_name='Количество'),
        ),
    ]
