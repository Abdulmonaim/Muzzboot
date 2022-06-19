# Generated by Django 4.0.5 on 2022-06-18 21:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('content', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='address',
            old_name='Address_active',
            new_name='Address_is_active',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Category_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Category_name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Category_product',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_content',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_discount',
            new_name='discount',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_purchase_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_quantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_description',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_user',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Category_content',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Category_meta_title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Category_parent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Product_meta_title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Product_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Product_sale_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Product_shop',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Product_type_product',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_vendor',
        ),
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='category',
            name='gender',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Product_review',
        ),
        migrations.DeleteModel(
            name='Product_type',
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
