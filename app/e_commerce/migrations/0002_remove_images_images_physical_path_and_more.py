# Generated by Django 4.0.5 on 2022-06-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='Images_physical_path',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Images_size',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Images_url',
        ),
        migrations.AddField(
            model_name='images',
            name='Images_img',
            field=models.ImageField(default='Null', upload_to=''),
            preserve_default=False,
        ),
    ]
