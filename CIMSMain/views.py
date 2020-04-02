from django.shortcuts import render
from .models import Meeting
from rest_framework import viewsets
from .serializers import MeetingSerializer
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers


def index(request):
    return render(request, 'index.html')
    

class MeetingViewSet(viewsets.ModelViewSet):
    """
    查看会议内容
    """
    queryset = Meeting.objects.all().order_by('-date')
    serializer_class = MeetingSerializer


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
                color = '#ff9f89'
            elif meeting.from_level.name == '市':
                color = '#98FB98'
            
            if meeting.meeting_status.name == '因故取消':
                continue
            meeting_list.append({
               'id': meeting.id,
               'mtitle': meeting.name,
               'mdate': meeting.date,
               'mcolor':color,               
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
           
            channel_list_str = '/'.join([channel.name for channel in channel_all])
            localchannel_list_str = '/'.join([channel.name for channel in localchannel_all])
                        
        except Meeting.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            'id': meeting.id,
            'mtitle': meeting.name,
            'mlocation':meeting.location.name,
            'mdate': meeting.date,
            'mschannel' : channel_list_str,
            'mlchannel' : localchannel_list_str,
            'mstaffs':meeting.staffs.name,
            'moffice':meeting.office.name,
            'mfromlevel':meeting.from_level.name,
            'mtolevel':meeting.to_level.name,
            'mstatus':meeting.meeting_status.name,
            'mremark':meeting.remark,
            # 'bpub_date': meeting.bpub_date,
            # 'bread': meeting.bread,
            # 'bcomment': meeting.bcomment,
            # 'image': meeting.image.url if book.image else ''
        })
