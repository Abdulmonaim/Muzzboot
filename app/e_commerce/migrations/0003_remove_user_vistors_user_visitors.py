# Generated by Django 4.0.5 on 2022-07-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0002_alter_user_followers_alter_user_vistors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='vistors',
        ),
        migrations.AddField(
            model_name='user',
            name='visitors',
            field=models.IntegerField(default=0),
        ),
    ]
