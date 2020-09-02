"""CIMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from CIMSMain import views

router = routers.DefaultRouter()
router.register(r'meeting', views.MeetingViewSet)


urlpatterns = [
    url('^$',views.chart),
    url('chart.html',views.chart),
    url('list.html',views.fullheight),

    url('list/(?P<pk>\d+)/$',views.list),
    url('lists/$',views.lists),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls), # 后台
    url(r'^api/meetings$', views.MeetingsAPIView.as_view(), name='meetings'), # 所有会议接口
    url(r'^api/meetings/(?P<pk>\d+)/$', views.MeetingAPIView.as_view(), name='meeting'), # 某会议查询接口
    
    url(r'^api/meetings/count/everymonth/thisyear/$', views.MeetingsCountEveryMonthThisYearView.as_view(), name='meetingcount'), # 今年所有会议
    url(r'^api/meetings/count/everymonth/lastyear/$', views.MeetingsCountEveryMonthLastYearView.as_view(), name='meetingcount'), # 去年所有会议

    url(r'^api/meetings/count/years/$', views.MeetingsCountYearsView.as_view(), name='meetingcount'), # 计算会议数量
    url(r'^api/meetings/count/offices/thisyear/$', views.MeetingsCountThisYearOfficeView.as_view(), name='meetingofficecountthisyear'), # 计算会议数量
    url(r'^api/meetings/count/offices/lastyear/$', views.MeetingsCountLastYearOfficeView.as_view(), name='meetingofficecountlastyear'), # 计算会议数量
]

