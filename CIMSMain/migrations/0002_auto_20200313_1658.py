# Generated by Django 2.2.10 on 2020-03-13 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CIMSMain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferenceroom',
            name='name',
            field=models.CharField(db_column='conferenceroom_name', max_length=64, verbose_name='会议室'),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='image',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='avatar/%Y/%m/', verbose_name='申请表'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='name',
            field=models.CharField(max_length=64, verbose_name='工作身份'),
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(max_length=64, verbose_name='级别'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='add_date',
            field=models.DateTimeField(db_column='add_date', verbose_name='创建条目日期'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateTimeField(db_column='meeting_time', verbose_name='会议时间'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='form_page',
            field=models.ForeignKey(db_column='form_page', on_delete=django.db.models.deletion.CASCADE, to='CIMSMain.FormPage', verbose_name='会议申请表'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='from_level',
            field=models.ForeignKey(db_column='from_level', on_delete=django.db.models.deletion.CASCADE, related_name='fromlevel', to='CIMSMain.Level', verbose_name='级别'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='location',
            field=models.ForeignKey(db_column='conference_room', on_delete=django.db.models.deletion.CASCADE, to='CIMSMain.ConferenceRoom', verbose_name='会议地点'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='modify_date',
            field=models.DateTimeField(db_column='modify_date', verbose_name='修改日期'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='name',
            field=models.CharField(db_column='meeting_name', max_length=128, verbose_name='会议名称'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='office',
            field=models.ForeignKey(db_column='office', on_delete=django.db.models.deletion.CASCADE, to='CIMSMain.Office', verbose_name='办会单位'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='staffs',
            field=models.ManyToManyField(to='CIMSMain.Staff', verbose_name='办会人员'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='to_level',
            field=models.ForeignKey(db_column='to_level', on_delete=django.db.models.deletion.CASCADE, related_name='tolevel', to='CIMSMain.Level', verbose_name='范围'),
        ),
        migrations.AlterField(
            model_name='office',
            name='name',
            field=models.CharField(max_length=64, verbose_name='单位'),
        ),
        migrations.AlterField(
            model_name='office',
            name='oset',
            field=models.ForeignKey(db_column='office_set', on_delete=django.db.models.deletion.CASCADE, to='CIMSMain.Set', verbose_name='机关'),
        ),
        migrations.AlterField(
            model_name='set',
            name='name',
            field=models.CharField(max_length=64, verbose_name='创建条目日期'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=64, verbose_name='工作人员'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='office',
            field=models.ForeignKey(db_column='staff_office', on_delete=django.db.models.deletion.CASCADE, to='CIMSMain.Office', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone1',
            field=models.CharField(max_length=64, verbose_name='电话1'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone2',
            field=models.CharField(max_length=64, verbose_name='电话2'),
        ),
    ]
