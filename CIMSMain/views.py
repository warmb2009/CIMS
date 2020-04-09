from django.shortcuts import render
from .models import Meeting
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


class MeetingViewSet(viewsets.ModelViewSet):
    """
    查看会议内容
    """
    queryset = Meeting.objects.all().order_by('-date')
    serializer_class = MeetingSerializer


class MeetingsCountYearsView(View):
    """
    查询今年会议数量
    """

    def get(self, request):
        """
        查询所有图书
        路由：GET /books/
        """
        info_dic = {}
        today = datetime.now()

        thisyear_count = Meeting.objects.filter(date__year=today.year).count()
        lastyear_count = Meeting.objects.filter(
            date__year=today.year-1).count()

        info_dic['thisyear'] = thisyear_count
        info_dic['lastyear'] = lastyear_count
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
