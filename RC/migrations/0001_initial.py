# Generated by Django 2.2.10 on 2020-03-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='省厅信道')),
            ],
            options={
                'verbose_name_plural': '省厅信道',
            },
        ),
        migrations.CreateModel(
            name='LocalChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='本地信道')),
            ],
            options={
                'verbose_name_plural': '本地信道',
            },
        ),
        migrations.CreateModel(
            name='RollCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': '点名情况',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='单位名称')),
            ],
            options={
                'verbose_name_plural': '单位名称',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='点名类型')),
            ],
            options={
                'verbose_name_plural': '点名类型',
            },
        ),
    ]
