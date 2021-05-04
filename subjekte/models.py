from django.db import models

# Create your models here.
class Shitesi(models.Model):
    emer = models.CharField(max_length=200)
    paga = models.IntegerField()

    def __str__(self):
        return self.emer


class Klienti(models.Model):
    emer = models.CharField(max_length=200)
    adrese = models.CharField(max_length=200)
    nipt = models.IntegerField()
    nr_tel = models.IntegerField()
    preferencial = models.BooleanField(default=False)

    def __str__(self):
        return self.emer


class Furnitori(models.Model):
    emer = models.CharField(max_length=200)
    adrese = models.CharField(max_length=200)
    nipt = models.IntegerField()
    nr_tel = models.IntegerField()
    preferencial = models.BooleanField(default=False)

    def __str__(self):
        return self.emer