from django.shortcuts import render
from .models import Meeting
from .models import Office

from rest_framework import viewsets
from .serializers import MeetingSerializer
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from datetime import datetime, timedelta


def index(request):
    return render(request, 'index.html')

def chart(request):
    return render(request, 'chart.html')

def fullheight(request):
    return render(request, 'full-height.html')

def lists(request):
    return list(request, 1)
    
def list(request, pk):
    if pk is not None:
        pk = int(pk)
        
    per_num = 20
    from_p = 0
    to_p = 10
        
    if pk is not None:
        from_p = (pk - 1) * per_num
        to_p = pk * per_num

    tables_count = Meeting.objects.count()
    table_list = Meeting.objects.order_by('-date')[from_p:to_p]

    context_list = []
    for item in table_list:
        new_item = {}
        
        new_item['name'] = item.name
        new_item['date'] = str(item.date)
        new_item['location'] = item.location.name


        channel_all = item.channel.all()                                    
        localchannel_all = item.local_channel.all()                         
                                                                                   
        channel_list_str = '/'.join([channel.name for channel in channel_all])                         
        localchannel_list_str = '/'.join([channel.name for channel in localchannel_all])
            
        new_item['channel'] = localchannel_list_str
        
        new_item['office'] = item.office.name
        new_item['level'] = item.from_level.name + '/' + item.to_level.name
        new_item['meeting_category'] = item.meeting_category.name
        new_item['remark'] = item.remark
        
        context_list.append(new_item)

    context = {"table_list" : context_list}
    pages = {}
    pages['pnumber'] = pk - 1
    pages['nnumber'] = pk + 1
    pages['current'] = pk

    all_num = tables_count // per_num + 1
    pages['num_pages'] = all_num
    pages['has_previous'] = True
    pages['has_next'] = True

    if pk >= all_num:
        pages['has_next'] = False

    if pk <= 1:
        pages['has_previous'] = False
    
    return render(request, 'list.html', {'table_list':context_list, 'pages':pages})


class MeetingsCountThisYearOfficeView(View):

    def get(self, request):
        """
        查询今年 各单位会议数量
        路由：GET /books/
        """
        info_list = []
        today = datetime.now()

        office_list = Office.objects.all()

        for office in office_list:
            office_id = office.id
            office_count = Meeting.objects.filter(office__id=office_id, date__year=today.year).count()
            if office_count == 0: # 数量为0的不计入
                continue
            
            office_info = {}
            office_info['name'] = office.name
            office_info['value'] = office_count

            info_list.append(office_info)

        return JsonResponse(info_list, safe=False)


class MeetingsCountLastYearOfficeView(View):

    def get(self, request):
        """
        查询去年 各单位会议数量
        路由：GET /books/
        """
        info_list = []
        today = datetime.now()

        office_list = Office.objects.all()

        for office in office_list:
            office_id = office.id
            
            office_count = Meeting.objects.filter(office__id=office_id, date__year=today.year-1).count()
            if office_count == 0: # 数量为0的不计入
                continue
            
            office_info = {}
            office_info['name'] = office.name
            office_info['value'] = office_count

            info_list.append(office_info)

        return JsonResponse(info_list, safe=False)


class MeetingViewSet(viewsets.ModelViewSet):
    """
    查看会议内容
    """
    queryset = Meeting.objects.all().order_by('-date')
    serializer_class = MeetingSerializer


class MeetingsCountYearsView(View):
    """
    查询今年及去年会议数量
    """

    def get(self, request):
        """
        查询今年及去年会议数量
        路由：GET /books/
        """
        info_dic = {}
        today = datetime.now()

        thisyear_count = Meeting.objects.filter(date__year=today.year).count()
        thismonth_count = Meeting.objects.filter(date__year=today.year, date__month=today.month).count()
        lastyear_count = Meeting.objects.filter(
            date__year=today.year-1).count()

        info_dic['thisyear'] = thisyear_count
        info_dic['lastyear'] = lastyear_count
        info_dic['thismonth'] = thismonth_count

        return JsonResponse(info_dic, safe=False)


class MeetingsCountEveryMonthThisYearView(View):
    """
    查询每月会议数量 今年
    """

    def get_all_data(self, month_list):
        today = datetime.now()
        data = []
        for month in month_list:
            queryset = Meeting.objects.filter(
                date__year=today.year, date__month=month)
            count = queryset.count()
            data.append((str(count) if count is not 0 else ''))
        return data

    def get_data_from_level(self, level, month_list):

        today = datetime.now()
        data = []
        for month in month_list:
            queryset = Meeting.objects.filter(
                date__year=today.year, date__month=month, from_level__name=level)
            count = queryset.count()
            data.append((str(count) if count is not 0 else ''))
        return data

    def get_month_str(self):
        month_list = []
        for month in range(12):
            month += 1
            month_str = (str(month) if month > 9 else ('0' + str(month)))
            month_list.append(month_str)
        return month_list

    def get(self, request):
        """
        查询所有会议
        路由：GET /meetings/
        """
        info_dic = {}
        categories = []

        month_list = self.get_month_str()
                
        for month in month_list:
            categories.append(month + '月')

        level1 = self.get_data_from_level('部', month_list)
        level2 = self.get_data_from_level('省', month_list)
        level3 = self.get_data_from_level('市', month_list)
        data = self.get_all_data(month_list)

        info_dic['categories'] = categories
        info_dic['level1'] = level1
        info_dic['level2'] = level2
        info_dic['level3'] = level3
        info_dic['data'] = data
        
        #print(categories)
        #print(level1)
        #print(level2)
        #print(level3)
        return JsonResponse(info_dic, safe=False)


class MeetingsCountEveryMonthLastYearView(View):
    """
    查询每月会议数量 去年
    """

    def get_all_data(self, month_list):
        today = datetime.now()
        data = []
        for month in month_list:
            queryset = Meeting.objects.filter(
                date__year=today.year-1, date__month=month)
            count = queryset.count()
            data.append((str(count) if count is not 0 else ''))
        return data

    def get_data_from_level(self, level, month_list):
        
        today = datetime.now()
        data = []
        for month in month_list:
            queryset = Meeting.objects.filter(
                date__year=today.year-1, date__month=month, from_level__name=level)
            count = queryset.count()
            data.append((str(count) if count is not 0 else ''))
        return data

    def get_month_str(self):
        month_list = []
        for month in range(12):
            month += 1
            month_str = (str(month) if month > 9 else ('0' + str(month)))
            month_list.append(month_str)
        return month_list

    def get(self, request):
        """
        查询所有图书
        路由：GET /books/
        """
        
        info_dic = {}
        categories = []

        month_list = self.get_month_str()
                
        for month in month_list:
            categories.append(month + '月')

        level1 = self.get_data_from_level('部', month_list)
        level2 = self.get_data_from_level('省', month_list)
        level3 = self.get_data_from_level('市', month_list)
        data = self.get_all_data(month_list)

        info_dic['categories'] = categories
        info_dic['level1'] = level1
        info_dic['level2'] = level2
        info_dic['level3'] = level3
        info_dic['data'] = data
        
        #print(categories)
        #print(level1)
        #print(level2)
        #print(level3)
        return JsonResponse(info_dic, safe=False)

class MeetingsAPIView(View):
    """
    查询所有会议
    """

    def get(self, request):
        """
        查询所有图书
        路由：GET /books/
        """
        queryset = Meeting.objects.all()
        meeting_list = []
        for meeting in queryset:
            color = ''
            if meeting.from_level.name == '省':
                color = '#A12F2F'
            elif meeting.from_level.name == '市':
                color = '#407434'
            elif meeting.from_level.name == '部':
                color = '#007bff'

            if meeting.meeting_status.name == '因故取消':
                continue
            meeting_list.append({
                'id': meeting.id,
                'mtitle': meeting.name,
                'mdate': meeting.date,
                'mcolor': color,
            })
        return JsonResponse(meeting_list, safe=False)


class MeetingAPIView(View):
    def get(self, request, pk):
        """
        获取单个会议信息
        路由： GET  /meetings/<pk>/
        """
        try:
            meeting = Meeting.objects.get(pk=pk)

            channel_all = meeting.channel.all()
            localchannel_all = meeting.local_channel.all()

            channel_list_str = '/'.join(
                [channel.name for channel in channel_all])
            localchannel_list_str = '/'.join(
                [channel.name for channel in localchannel_all])

        except Meeting.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            'id': meeting.id,
            'mtitle': meeting.name,
            'mlocation': meeting.location.name,
            'mdate': meeting.date,
            'mschannel': channel_list_str,
            'mlchannel': localchannel_list_str,
            'mstaffs': meeting.staffs.name,
            'moffice': meeting.office.name,
            'mfromlevel': meeting.from_level.name,
            'mtolevel': meeting.to_level.name,
            'mstatus': meeting.meeting_status.name,
            'mremark': meeting.remark,
            # 'bpub_date': meeting.bpub_date,
            # 'bread': meeting.bread,
            # 'bcomment': meeting.bcomment,
            # 'image': meeting.image.url if book.image else ''
        })
