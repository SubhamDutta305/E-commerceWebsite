# Generated by Django 3.0.4 on 2020-03-31 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
    ]
