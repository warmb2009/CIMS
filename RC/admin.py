from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Daily)
admin.site.register(RollCall)
admin.site.register(OrderSet)
admin.site.register(OrderReturn)
admin.site.register(RollType)
admin.site.register(RollChannel)

