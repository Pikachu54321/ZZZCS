# Generated by Django 2.1.5 on 2023-06-06 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20230606_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='classification',
            field=models.ForeignKey(db_constraint=False, default='', on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Classification', verbose_name='分类'),
        ),
    ]