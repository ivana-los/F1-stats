from django.apps import AppConfig
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Driver)
admin.site.register(Constructor)
admin.site.register(Season)
admin.site.register(Race)
admin.site.register(Result)
admin.site.register(LapData)
admin.site.register(PitStop)
admin.site.register(Prediction)
