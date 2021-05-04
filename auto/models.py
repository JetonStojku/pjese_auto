from django.db import models

# Create your models here.
class Marka(models.Model):
    emer = models.CharField(max_length=200)

    def __str__(self):
        return self.emer


class Kategoria(models.Model):
    emer = models.CharField(max_length=200)

    def __str__(self):
        return self.emer


class Lenda_Djegese(models.Model):
    emer = models.CharField(max_length=200)

    def __str__(self):
        return self.emer
