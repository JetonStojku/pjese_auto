from django.contrib import admin
from .models import Koke_Fature, Rrjesht_Fature


class Koke_FatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'shites', 'klient')


admin.site.register(Koke_Fature, Koke_FatureAdmin)



class Rrjesht_FatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'fature_id', 'produkt_id', 'sasia', 'cmimi', 'zbritje', 'tvsh')


admin.site.register(Rrjesht_Fature, Rrjesht_FatureAdmin)

