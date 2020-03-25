from django.shortcuts import render
from .models import Meeting
from rest_framework import viewsets
from .serializers import MeetingSerializer
from django.views.generic.base import View
from django.http import HttpResponse,JsonResponse


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
           meeting_list.append({
               'id': meeting.id,
               'mtitle': meeting.name,
               'mdate': meeting.date,               
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
       except Meeting.DoesNotExist:
           return HttpResponse(status=404)

       return JsonResponse({
           'id': meeting.id,
           'btitle': meeting.name,
           #'bpub_date': meeting.bpub_date,
           #'bread': meeting.bread,
           #'bcomment': meeting.bcomment,
           #'image': meeting.image.url if book.image else ''
       })