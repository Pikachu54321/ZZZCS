# Generated by Django 2.1.5 on 2023-07-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20230606_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=32, verbose_name='物资名称'),
        ),
    ]
