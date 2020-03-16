from django.db import models
from CIMSMain.models import Channel


class RollTime(models.Model):
    '''存储日常点名时间 9:00 9:30 等等其他时间'''
    time = models.TimeField(verbose_name='点名时间', blank=True, null=True)
    
    def __str__(self):
        return str(self.time)

    class Meta:
        verbose_name_plural = '点名时间'
        

class RollCall(models.Model):
    '''存储点名情况'''
    channel = models.ForeignKey('RollChannel', on_delete=models.CASCADE, verbose_name='点名信道', default=None, null=True, blank=True)
    time = models.ForeignKey('RollTime', on_delete=models.CASCADE, verbose_name='点名时间', default=None, null=True, blank=True)
    roll_type = models.ForeignKey('RollType', on_delete=models.CASCADE, verbose_name='点名类型', default=None, null=True, blank=True)
    order_set = models.ForeignKey('OrderSet', on_delete=models.CASCADE, verbose_name='被点名人', default=None, null=True, blank=True)
    order_return = models.ForeignKey('OrderReturn', on_delete=models.CASCADE, verbose_name='点名结果', default=None, null=True, blank=True)
    daily_record = models.DateField(verbose_name='点名日期', blank=True, null=True)
    remark = models.CharField(max_length=512, verbose_name="备注", blank=True)
    
    def __str__(self):
        re_str = str(self.daily_record) + '  \t' + self.roll_type.name + '  \t' + str(self.time.time) + '\t  被点单位:  \t' + self.order_set.name + '\t\t  ' + self.order_return.name  
        return re_str
#        return order_return.name

    class Meta:
        verbose_name_plural = '点名情况'

    
class OrderSet(models.Model):
    '''存储需要点名的单位'''
    name = models.CharField(max_length=32, verbose_name="单位名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '单位名称'


class OrderReturn(models.Model):
    '''存储点名结果 应答/未应答'''
    name = models.CharField(max_length=32, verbose_name="点名结果")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '点名结果'


class RollType(models.Model):
    '''存储点名级别 省厅点名/市局点名'''
    name = models.CharField(max_length=32, verbose_name="点名类型")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '点名类型'

    
class RollChannel(models.Model):
    '''存储点名信道 山东1 2 4 5 省指 泰安1 2 市指'''
    name = models.CharField(max_length=32, verbose_name="点名信道")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '点名信道'
        
