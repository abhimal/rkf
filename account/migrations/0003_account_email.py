# Generated by Django 3.0.5 on 2020-05-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200309_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(default='xyz@gmail.com', max_length=64),
        ),
    ]
