# Generated by Django 2.2.10 on 2020-04-01 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CIMSMain', '0009_channel_sign'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='会议状态')),
            ],
            options={
                'verbose_name_plural': '会议状态',
            },
        ),
        migrations.AlterModelOptions(
            name='meeting',
            options={'verbose_name_plural': '会议汇总'},
        ),
        migrations.AlterModelOptions(
            name='office',
            options={'verbose_name_plural': '办会单位'},
        ),
        migrations.AlterModelOptions(
            name='set',
            options={'verbose_name_plural': '所属机关'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name_plural': '工作人员汇总'},
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='add_date',
        ),
        migrations.AlterField(
            model_name='office',
            name='oset',
            field=models.ForeignKey(db_column='office_set', on_delete=django.db.models.deletion.CASCADE, to='CIMSMain.Set', verbose_name='所属机关'),
        ),
        migrations.AlterField(
            model_name='set',
            name='name',
            field=models.CharField(max_length=64, verbose_name='机关名称'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_status',
            field=models.ForeignKey(db_column='meeting_status', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetingstatus', to='CIMSMain.MeetingStatus', verbose_name='会议状态'),
        ),
    ]