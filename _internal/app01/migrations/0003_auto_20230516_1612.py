# Generated by Django 2.1.5 on 2023-05-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20230511_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateField(verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '钢管'), (2, '物资'), (3, '弯头钢管')], verbose_name='性别'),
        ),
    ]
