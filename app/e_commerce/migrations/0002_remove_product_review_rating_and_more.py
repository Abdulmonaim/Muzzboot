# Generated by Django 4.0.5 on 2022-07-03 00:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='review_rating',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]