from django.db import models
import django.utils.timezone as timezone

'''
会议信息
'''
class Meeting(models.Model):
    # 会议名称 字符串
    name = models.CharField(max_length=128, db_column='meeting_name', verbose_name='会议名称')

    # 会议时间 django date
    date = models.DateTimeField(db_column='meeting_time', verbose_name='会议时间')
    
    # 会议地点 外键
    location = models.ForeignKey('ConferenceRoom', db_column='conference_room', on_delete=models.CASCADE, verbose_name='会议地点')

    # 会议信道
    channel = models.ManyToManyField('Channel', db_column='channel', verbose_name='省级会议信道', blank=True)

    # 市局信道
    local_channel = models.ManyToManyField('LocalChannel', db_column='local_channel', verbose_name='市级会议信道', blank=True)
    
    # 办会人员 多对多
    staffs = models.ManyToManyField('Staff', verbose_name='办会人员')

    # 办会单位 外键
    office = models.ForeignKey('Office', db_column='office', on_delete=models.CASCADE, verbose_name='办会单位')

    # 会议申请表(扫描件 图片) 外键
    form_page = models.ForeignKey('FormPage', db_column='form_page', on_delete=models.CASCADE, verbose_name='会议申请表', null=True, blank=True)

    # 办会级别 (部 省 市 县 科所) 外键
    from_level = models.ForeignKey('Level', db_column='from_level', on_delete=models.CASCADE, related_name='fromlevel', verbose_name='级别')
    
    # 开至级别 (部 省 市 县 科所) 外键
    to_level = models.ForeignKey('Level', db_column='to_level', on_delete=models.CASCADE, related_name='tolevel', verbose_name='范围')

    # 会议状态 已发布 未发布 因故延期 因故取消
    meeting_status = models.ForeignKey('MeetingStatus', db_column='meeting_status', verbose_name='会议状态', on_delete=models.CASCADE, related_name='meetingstatus', default=1)

    # 会议类型 视频会议 本地会议等
    meeting_category = models.ForeignKey('MeetingCategory', db_column='meeting_category', verbose_name='会议类型', on_delete=models.CASCADE, related_name='meetingcategory', default=1)

    remark = models.CharField(max_length=256, db_column='meeting_remark', verbose_name='备注', default='', null=True)

    # 修改日期 date
    modify_date = models.DateTimeField(db_column='modify_date', verbose_name='最后修改日期', auto_now = True)
    
    def __str__(self):
        return str(self.date) + '\t' + self.name + '\t(' +self.location.name + '--\t' +self.office.name + ')'

    class Meta:
        verbose_name_plural='会议汇总'

        
# 会议室
class ConferenceRoom(models.Model):

    name = models.CharField(max_length=64, db_column='conferenceroom_name', verbose_name='会议室')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='会议室'

        
# 单位
class Office(models.Model):
    name = models.CharField(max_length=64, verbose_name='单位')
    oset = models.ForeignKey('Set', db_column='office_set', on_delete=models.CASCADE, verbose_name='所属机关')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='办会单位'

        
# 机关
class Set(models.Model):
    name = models.CharField(max_length=64, verbose_name='机关名称')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='所属机关'

        
# 工作人员
class Staff(models.Model):
    name = models.CharField(max_length=64, verbose_name='工作人员')
    phone1 = models.CharField(max_length=64, verbose_name='电话1') # 电话1
    phone2 = models.CharField(max_length=64, verbose_name='电话2', blank=True) # 电话2

    office = models.ForeignKey('Office', db_column='staff_office', on_delete=models.CASCADE, verbose_name='')

    def __str__(self):
        return self.name + '   ------    ' + self.office.name
    
    class Meta:
        verbose_name_plural='工作人员汇总'

        
# 工作身份 负责人 工作人员 两种    
class Identity(models.Model):
    name = models.CharField(max_length=64, verbose_name='工作身份')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='工作身份'

        
# 申请表
class FormPage(models.Model):
    image = models.ImageField(max_length=1000,upload_to='avatar/%Y/%m/', verbose_name=u'申请表', null=True, blank=True, )

    class Meta:
        verbose_name_plural='申请表'
        

# Level 等级 部 省 市 县 科所队
class Level(models.Model):
    name = models.CharField(max_length=64, verbose_name='级别')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='级别'


# 省级信道
class Channel(models.Model):
    name = models.CharField(max_length=64, verbose_name='省级信道')
    sign = models.CharField(max_length=64, verbose_name='标志', blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='省级信道'

# 市级信道
class LocalChannel(models.Model):
    name = models.CharField(max_length=64, verbose_name='市级信道')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='市级信道'

# 市级信道
class MeetingStatus(models.Model):
    name = models.CharField(max_length=64, verbose_name='会议状态')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='会议状态'

# 会议种类
class MeetingCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name='会议类型')
    remark = models.CharField(max_length=256, verbose_name='备注', default='')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='会议类型'
