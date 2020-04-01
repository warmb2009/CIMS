from django.contrib import admin
from .models import *


class MeetingInfoAdmin(admin.ModelAdmin):
    
    list_display = ('name','from_level', 'date', 'office', 'location')
    search_fields = ('name', 'from_level', 'date', 'office', 'location')
    list_filter = ('from_level', 'name', 'date', 'office', 'location')
     

admin.site.register(Meeting, MeetingInfoAdmin)
#admin.site.register(ConferenceRoom)
admin.site.register(Office)
admin.site.register(Set)
admin.site.register(Staff)
#admin.site.register(Identity)
#admin.site.register(FormPage)
#admin.site.register(Level)
#admin.site.register(Channel)
#admin.site.register(LocalChannel)
#admin.site.register(MeetingStatus)
#admin.site.register(MeetingCategory)


