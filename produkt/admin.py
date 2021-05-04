from django.contrib import admin
from .models import Produkt


class ProduktAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial', 'vit_prodhimi_f', 'vit_prodhimi_m', 'marka', 'kategoria', 'lenda_djegese', 'cmim_sh')


admin.site.register(Produkt, ProduktAdmin)
