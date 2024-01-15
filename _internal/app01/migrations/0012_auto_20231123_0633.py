# Generated by Django 2.2 on 2023-11-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_merge_20231123_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='classification',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=32, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '已到货'), (2, '未到货'), (3, '已出库'), (4, '未出库')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='level',
            field=models.SmallIntegerField(choices=[(1, '1级'), (2, '2级'), (3, '3级'), (4, '4级')], default=1, verbose_name='种类'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='mobile',
            field=models.CharField(max_length=50, verbose_name='物资编号'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='price',
            field=models.IntegerField(default=0, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '已到货'), (2, '未到货'), (3, '已出库'), (4, '未出库')], default=2, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateField(verbose_name='入库时间'),
        ),
        migrations.DeleteModel(
            name='Classification',
        ),
    ]