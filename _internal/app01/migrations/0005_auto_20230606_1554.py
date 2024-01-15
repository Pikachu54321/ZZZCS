# Generated by Django 2.1.5 on 2023-06-06 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20230517_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='分类')),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='gender',
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='level',
            field=models.SmallIntegerField(choices=[(1, '弯头'), (2, '直管'), (3, '膨胀螺丝'), (4, '普通螺丝')], default=1, verbose_name='种类'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '已出库'), (2, '在库')], default=2, verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='classification',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app01.Classification', verbose_name='分类'),
        ),
    ]