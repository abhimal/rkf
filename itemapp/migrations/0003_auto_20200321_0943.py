# Generated by Django 2.1.2 on 2020-03-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemapp', '0002_auto_20200317_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='selling_price',
            field=models.FloatField(default='0.0'),
        ),
    ]
