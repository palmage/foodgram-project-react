# Generated by Django 3.0.5 on 2021-09-14 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_favorite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'verbose_name_plural': 'Подписки'},
        ),
        migrations.AlterModelOptions(
            name='ingredientrecipe',
            options={'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name_plural': 'Подписки'},
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='lower',
            new_name='lover',
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('lover', 'recipe'), name='unique_Favorite'),
        ),
    ]