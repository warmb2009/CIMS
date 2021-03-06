# Generated by Django 2.2.10 on 2020-03-14 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CIMSMain', '0004_auto_20200314_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='form_page',
            field=models.ForeignKey(blank=True, db_column='form_page', null=True, on_delete=django.db.models.deletion.CASCADE, to='CIMSMain.FormPage', verbose_name='会议申请表'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone2',
            field=models.CharField(blank=True, max_length=64, verbose_name='电话2'),
        ),
    ]
