# Generated by Django 4.2 on 2023-04-17 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_store_custo_last_na_12c8c5_idx_store_custo_last_na_2e448d_idx_and_more'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='customer',
            new_name='store_Custo_last_na_12c8c5_idx',
            old_name='store_custo_last_na_2e448d_idx',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_Customers',
        ),
    ]
