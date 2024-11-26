# Generated by Django 5.1.3 on 2024-11-26 18:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_transaction_transaction_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='total_sale',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='supplier',
            name='total_purchase',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
