from django.shortcuts import render
from .models import Meeting
from rest_framework import viewsets
from .serializers import MeetingSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    """
    查看会议内容
    """
    queryset = Meeting.objects.all().order_by('-date')
    serializer_class = MeetingSerializer
