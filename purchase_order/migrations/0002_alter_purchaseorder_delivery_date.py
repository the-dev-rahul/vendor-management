# Generated by Django 5.0.6 on 2024-05-22 17:11

import purchase_order.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(default=purchase_order.models.add_two_days),
        ),
    ]