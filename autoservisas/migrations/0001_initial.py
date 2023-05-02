# Generated by Django 4.2 on 2023-05-01 20:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('plate_nr', models.CharField(max_length=20)),
                ('vin_number', models.CharField(max_length=17)),
                ('client', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('car_model_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('car_model', models.CharField(max_length=100, verbose_name='Car model')),
                ('year', models.DateField(null=True, verbose_name='Made on:')),
                ('engine', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Car Model',
                'verbose_name_plural': 'Car Models',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='ServicePrice',
            fields=[
                ('service_price_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField(verbose_name='Price')),
                ('cars', models.ManyToManyField(to='autoservisas.carmodel')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.service')),
            ],
            options={
                'verbose_name': 'Service Price',
                'verbose_name_plural': 'Service Prices',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.car')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.service')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.carmodel'),
        ),
    ]