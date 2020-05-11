# Generated by Django 2.1.2 on 2020-03-16 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=64)),
                ('brand_name', models.CharField(max_length=64)),
                ('item_size', models.CharField(max_length=64)),
                ('item_color', models.CharField(max_length=64)),
                ('item_unit', models.CharField(max_length=64)),
                ('item_quantity', models.IntegerField()),
                ('purchase_price', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('mrp', models.FloatField()),
                ('item_code', models.CharField(max_length=64)),
                ('item_level', models.IntegerField(default='0')),
                ('item_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesman', models.CharField(max_length=64)),
                ('return_dt', models.DateTimeField(auto_now_add=True)),
                ('return_d', models.DateField(auto_now_add=True)),
                ('return_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itemapp.Items')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=64)),
                ('salesman', models.CharField(max_length=64)),
                ('mobile_number', models.CharField(max_length=64)),
                ('sale_price', models.FloatField()),
                ('comission', models.FloatField()),
                ('exchange_item', models.BooleanField(default=False)),
                ('return_item', models.CharField(max_length=64)),
                ('sale_dt', models.DateTimeField(auto_now_add=True)),
                ('sale_d', models.DateField(auto_now_add=True)),
                ('sales_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itemapp.Items')),
            ],
        ),
    ]
