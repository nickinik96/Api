# Generated by Django 4.2 on 2023-04-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_address_zip'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_Custo_last_na_12c8c5_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_Customers',
        ),
    ]
