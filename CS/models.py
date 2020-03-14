from django.db import models

# Create your models here.

class Staff(models.Model):
     
    name = models.CharField(max_length=32, verbose_name='姓名')    
    title = models.ForeignKey('Title', on_delete=models.CASCADE, verbose_name='职务')
    phone1 = models.CharField(max_length=64, verbose_name='联系方式')
    phone2 = models.CharField(max_length=64, verbose_name='联系方式2', blank=True)

    Set = models.ForeignKey('Set', on_delete=models.CASCADE, verbose_name='单位')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='保障专班'
        

# 单位
class Set(models.Model):
    name = models.CharField(max_length=64, verbose_name='单位')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='单位'


class Title(models.Model):
    name = models.CharField(max_length=64, verbose_name='职务')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='职务'
