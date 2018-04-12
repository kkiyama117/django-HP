from django.contrib import admin
from django.contrib.admin import models

from .models import Trans, Station, Route, Train


class TrainAdmin(admin.ModelAdmin):
    pass


admin.site.register(Trans)
admin.site.register(Station)
admin.site.register(Route)
admin.site.register(Train)
