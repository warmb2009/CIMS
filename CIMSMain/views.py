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
        lastyear_count = Meeting.objects.filter(date__year=today.year-1).count()

    
        info_dic['thisyear'] = thisyear_count
        info_dic['lastyear'] = lastyear_count
        return JsonResponse(info_dic, safe=False)

class MeetingsCountEveryMonthThisYearView(View):
    """
    查询每月会议数量
    """

    def get(self, request):
        """
        查询所有图书
        路由：GET /books/
        """
        info_dic = {}

        categories = []
        data = []

        # meeings date
        today = datetime.now()
        for month in range(12):
            month += 1
            month_str = (str(month) if month > 9 else ('0' + str(month)))
            queryset = Meeting.objects.filter(
                date__year=today.year, date__month=month_str)
            count = queryset.count()

            categories.append(str(month) + '月')
            data.append((str(count) if count is not 0 else ''))
            # print(month_str + '月:' + str(count))

        info_dic['categories'] = categories
        info_dic['data'] = data
        return JsonResponse(info_dic, safe=False)


class MeetingsCountEveryMonthLastYearView(View):
    """
    查询每月会议数量
    """

    def get(self, request):
        """
        查询所有图书
        路由：GET /books/
        """
        info_dic = {}

        categories = []
        data = []

        # meeings date
        today = datetime.now()
        for month in range(12):
            month += 1
            month_str = (str(month) if month > 9 else ('0' + str(month)))
            queryset = Meeting.objects.filter(
                date__year=today.year-1, date__month=month_str)
            count = queryset.count()

            categories.append(str(month) + '月')
            data.append(str(count))
            # print(month_str + '月:' + str(count))

        info_dic['categories'] = categories
        info_dic['data'] = data
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
