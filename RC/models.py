from django.db import models
from CIMSMain.models import Channel

# Create your models here.

class Daily(models.Model):
    datetime = models.DateField(verbose_name='点名日期')

    channel = models.OneToOneField('RollCall', on_delete=models.CASCADE, verbose_name='点名列表', blank=True, null=True)
        
    def __str__(self):
        return str(self.datetime)

    class Meta:
        verbose_name_plural = '日常点名'

# 省厅点名
class RollCall(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name='点名信道', blank=True, null=True)
    time = models.TimeField(verbose_name='点名时间', blank=True, null=True)
    roll_type = models.ForeignKey('RollType', on_delete=models.CASCADE, verbose_name='点名类型', blank=True, null=True)
    order_return = models.ForeignKey('OrderReturn', on_delete=models.CASCADE, verbose_name='点名结果', blank=True, null=True)
    
#    def _j_str__(self):
#        return order_return.name

    class Meta:
        verbose_name_plural = '点名情况'

# 市局点名
class CityRollCall(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name='点名信道', blank=True, null=True)
    time = models.TimeField(verbose_name='点名时间', blank=True, null=True)
    roll_type = models.ForeignKey('RollType', on_delete=models.CASCADE, verbose_name='点名类型', blank=True, null=True)
    order_return = models.ForeignKey('OrderReturn', on_delete=models.CASCADE, verbose_name='点名结果', blank=True, null=True)
    
#    def __str__(self):
#        return order_return.name

    class Meta:
        verbose_name_plural = '点名情况'

    
# 要点名的单位名称        
class OrderSet(models.Model):
    name = models.CharField(max_length=32, verbose_name="单位名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '单位名称'

# 点名结果
class OrderReturn(models.Model):
    name = models.CharField(max_length=32, verbose_name="点名结果")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '点名结果'


class RollType(models.Model):
    name = models.CharField(max_length=32, verbose_name="点名类型")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '点名级别'
        
