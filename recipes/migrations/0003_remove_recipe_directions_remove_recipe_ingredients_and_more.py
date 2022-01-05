# Generated by Django 4.0 on 2021-12-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='directions',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]