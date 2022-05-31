# Generated by Django 4.0.3 on 2022-05-22 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0008_remove_user_user_intro_remove_user_user_profile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address_address', models.CharField(max_length=50)),
                ('Address_zipcode', models.CharField(max_length=50)),
                ('Address_active', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='User_active',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='User_user_name',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='User_admin',
            field=models.BooleanField(),
        ),
        migrations.AddField(
            model_name='user',
            name='User_Address',
            field=models.ManyToManyField(to='e_commerce.address'),
        ),
    ]
