# Generated by Django 3.0.5 on 2020-05-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemapp', '0010_auto_20200509_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='dump_stock',
            field=models.IntegerField(default='0'),
        ),
    ]
