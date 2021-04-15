from datetime import datetime

from django.db import models


# Create your models here.
class Produkt(models.Model):
    # realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    serial = models.CharField(max_length=200)
    vit_prodhimi_f = models.IntegerField()
    vit_prodhimi_m = models.IntegerField()
    # price = models.IntegerField()
    # bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    # photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # is_published = models.BooleanField(default=True)
    # list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
