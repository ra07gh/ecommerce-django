# Generated by Django 4.2.20 on 2025-03-17 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0003_product_net'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='notes',
            field=models.CharField(default='', max_length=50),
        ),
    ]
