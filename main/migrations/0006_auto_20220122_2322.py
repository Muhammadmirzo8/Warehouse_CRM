# Generated by Django 3.2.9 on 2022-01-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_stats_product_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='in_warehouse',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='product_amount',
            field=models.PositiveIntegerField(),
        ),
    ]
