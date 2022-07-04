# Generated by Django 4.0.5 on 2022-07-04 02:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('mobile', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=75)),
                ('followers', models.IntegerField(default=0)),
                ('visitors', models.IntegerField(default=0)),
                ('user_json', models.JSONField(blank=True, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('cup_size', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('size_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('human_parsing', models.ImageField(blank=True, null=True, upload_to='')),
                ('user_size', models.CharField(blank=True, max_length=7, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('shipping_charge', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('cart_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=75)),
                ('category_gender', models.BooleanField(default=True)),
                ('category_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Checked_cart',
            fields=[
                ('checked_cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cart_total', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('shipping_charge', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('user_id', models.IntegerField(default=0)),
                ('checked_cart_selling_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100)),
                ('product_details', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_discount', models.DecimalField(decimal_places=2, default=False, max_digits=5)),
                ('product_brand', models.CharField(max_length=75)),
                ('quantity', models.IntegerField()),
                ('quantity_alarm', models.CharField(max_length=100)),
                ('product_date_entry', models.DateField()),
                ('product_rating', models.DecimalField(decimal_places=1, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('product_category', models.ManyToManyField(to='e_commerce.category')),
                ('product_color', models.ManyToManyField(to='e_commerce.color')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=7)),
                ('size_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_rating', models.DecimalField(decimal_places=1, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('review_content', models.TextField()),
                ('review_date', models.DateField()),
                ('review_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.product')),
                ('review_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_size',
            field=models.ManyToManyField(to='e_commerce.size'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images_img', models.ImageField(upload_to='')),
                ('images_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce.category')),
                ('images_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='Checked_cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_cart_item_title', models.CharField(max_length=75)),
                ('checked_cart_item_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('checked_cart_item_size', models.CharField(max_length=7)),
                ('checked_cart_item_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('checked_cart_item_quntity', models.IntegerField(default=1)),
                ('product_id', models.IntegerField(default=0)),
                ('checked_cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.checked_cart')),
                ('sales', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.sales')),
            ],
        ),
        migrations.CreateModel(
            name='Cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_item_title', models.CharField(max_length=75)),
                ('cart_item_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('cart_item_size', models.CharField(max_length=7)),
                ('cart_item_color', models.CharField(max_length=7)),
                ('cart_item_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cart_item_quntity', models.IntegerField(default=1)),
                ('cart_item_cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.cart')),
                ('cart_item_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.product')),
            ],
        ),
    ]
