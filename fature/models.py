from datetime import datetime
from django.db import models
from subjekte.models import Shitesi, Klienti
from produkt.models import Produkt

class Koke_Fature(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    shites = models.ForeignKey(Shitesi, on_delete=models.DO_NOTHING)
    klient = models.ForeignKey(Klienti, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.date




class Rrjesht_Fature(models.Model):
    fature_id = models.ForeignKey(Koke_Fature, on_delete=models.DO_NOTHING)
    produkt_id = models.ForeignKey(Produkt, on_delete=models.DO_NOTHING)
    sasia = models.IntegerField()
    cmimi = models.IntegerField()
    zbritje = models.IntegerField()
    tvsh = models.IntegerField()


    def __str__(self):
        return self.fature_id