# Generated by Django 4.2.20 on 2025-03-20 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeautyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم الفئة')),
                ('description', models.TextField(verbose_name='وصف الفئة')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='ملاحظات')),
            ],
        ),
    ]
