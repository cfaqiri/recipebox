# Generated by Django 4.0 on 2021-12-30 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_remove_recipe_directions_remove_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(default='blank', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='url',
            field=models.URLField(default='blank'),
            preserve_default=False,
        ),
    ]
