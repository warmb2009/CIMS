from django.db import models


class Staff(models.Model):
    ''' 人员 '''     
    name = models.CharField(max_length=32, verbose_name='姓名')    
    title = models.ForeignKey('Title', on_delete=models.CASCADE, verbose_name='职务')
    phone1 = models.CharField(max_length=64, verbose_name='联系方式')
    phone2 = models.CharField(max_length=64, verbose_name='联系方式2', blank=True)

    Set = models.ForeignKey('Set', on_delete=models.CASCADE, verbose_name='单位')
    
    def __str__(self):
        return self.Set.name + '\t' + self.name + ' (电话: ' + self.phone1 + ') '

    class Meta:
        verbose_name_plural='保障专班'


class Set(models.Model):
    '''单位'''
    name = models.CharField(max_length=64, verbose_name='单位')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='单位'


class Title(models.Model):
    '''职务'''
    name = models.CharField(max_length=64, verbose_name='职务')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='职务'
