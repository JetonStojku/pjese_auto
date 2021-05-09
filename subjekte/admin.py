from django.contrib import admin
from .models import Shitesi, Klienti, Furnitori


class ShitesiAdmin(admin.ModelAdmin):
    list_display = ('id', 'emer', 'paga')


admin.site.register(Shitesi, ShitesiAdmin)



class KlientiAdmin(admin.ModelAdmin):
    list_display = ('id', 'emer', 'adrese', 'nipt', 'nr_tel', 'preferencial')


admin.site.register(Klienti, KlientiAdmin)



class FurnitoriAdmin(admin.ModelAdmin):
    list_display = ('id', 'emer', 'adrese', 'nipt', 'nr_tel', 'preferencial')


admin.site.register(Furnitori, FurnitoriAdmin)

