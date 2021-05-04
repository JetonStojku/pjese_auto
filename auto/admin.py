from django.contrib import admin
from .models import Marka


class MarkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'emer')

admin.site.register(Marka, MarkaAdmin)
