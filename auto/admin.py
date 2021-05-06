from django.contrib import admin
from .models import Marka, Lenda_Djegese, Kategoria


class MarkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'emer')


admin.site.register(Marka, MarkaAdmin)


class LendaDjegseAdmin(admin.ModelAdmin):
    list_display = ('id', 'emer')


admin.site.register(Lenda_Djegese, MarkaAdmin)


class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'emer')


admin.site.register(Kategoria, MarkaAdmin)
