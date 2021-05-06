from datetime import datetime

from django.db import models
from auto.models import Marka, Kategoria, Lenda_Djegese


# Create your models here.
class Produkt(models.Model):
    # realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    serial = models.CharField(max_length=200)
    vit_prodhimi_f = models.IntegerField()
    vit_prodhimi_m = models.IntegerField()
    marka = models.ForeignKey(Marka, on_delete=models.DO_NOTHING)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.DO_NOTHING)
    lenda_djegese = models.ForeignKey(Lenda_Djegese, on_delete=models.DO_NOTHING)
    cmim_b = models.IntegerField()
    cmim_sh = models.IntegerField()
    sasia = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.serial
