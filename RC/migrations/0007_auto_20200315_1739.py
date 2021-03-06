# Generated by Django 2.2.10 on 2020-03-15 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RC', '0006_auto_20200315_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='RollChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='点名信道')),
            ],
            options={
                'verbose_name_plural': '点名信道',
            },
        ),
        migrations.AlterField(
            model_name='rollcall',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RC.RollChannel', verbose_name='点名信道'),
        ),
        migrations.AlterField(
            model_name='rolltype',
            name='name',
            field=models.CharField(max_length=32, verbose_name='点名级别'),
        ),
    ]
