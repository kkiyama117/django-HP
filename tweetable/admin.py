from django.contrib import admin

from .models import *


class TrainAdmin(admin.ModelAdmin):
    pass


admin.site.register(User)
admin.site.register(Tweet)
