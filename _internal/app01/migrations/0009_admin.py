# Generated by Django 2.1.5 on 2023-08-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20230809_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
    ]
