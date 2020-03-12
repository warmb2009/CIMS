from django.db import models

'''

'''
class Meeting(models.Model):
    # 会议名称 字符串
    name = models.CharField(max_length=128, db_column='meeting_name')

    # 会议时间 django date
    date = models.DateTimeField(db_column='meeting_time')
    
    # 会议地点 外键
    location = models.ForeignKey('ConferenceRoom', db_column='conference_room', on_delete=models.CASCADE)

    # 办会人员 多对多
    staffs = models.ManyToManyField('Staff')

    # 办会单位 外键
    office = models.ForeignKey('Office', db_column='office', on_delete=models.CASCADE)

    # 会议申请表(扫描件 图片) 外键
    form_page = models.ForeignKey('FormPage', db_column='form_page', on_delete=models.CASCADE)

    # 办会级别 (部 省 市 县 科所) 外键
    from_level = models.ForeignKey('Level', db_column='from_level', on_delete=models.CASCADE)
    
    # 开至级别 (部 省 市 县 科所) 外键
    to_level = models.ForeignKey('Level', db_column='to_level', on_delete=models.CASCADE)

    # 创建条目日期 date
    add_date = models.DateTimeField(db_column='add_date')

    # 修改日期 date
    modify_date = models.DateTimeField(db_column='modify_date')

    
    def __str__(self):
        return self.name

# 会议室
class ConferenceRoom(models.Model):

    name = models.CharField(max_length=64, db_column='conferenceroom_name')
    def __str__(self):
        return self.name

# 单位
class Office(models.Model):
    name = models.CharField(max_length=64)
    set = ForeignKey()
    def __str__(self):
        return self.name
    
# 机关
class Set(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

# 工作人员
class Staff(models.Model):
    name = models.CharField(max_length=64)
    phone1 = models.CharField(max_length=64) # 电话1
    phone2 = models.CharField(max_length=64) # 电话2
    office = ForeignKey('Office')

# 工作身份 负责人 工作人员 两种    
class Identity(models.Model):
    name = models.CharField(max_length=64)

# 申请表
class FormPage(models.Model):
    Image = Image() # 图片类

# Level 等级 部 省 市 县 科所队
class Level(models.Model):
    name = models.CharField(max_length=64)


