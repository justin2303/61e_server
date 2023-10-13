from django.db import models


# Create your models here.
class Player(models.Model):
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    GUID = models.CharField(max_length=8)
    user_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user_name}: has {self.kills} kills with an ID of {self.GUID}"

class Regiments(models.Model):
    reg_61e = models.IntegerField(default=0)
    reg_CSC = models.IntegerField(default=0)
    reg_84th = models.IntegerField(default=0)
    reg_85th = models.IntegerField(default=0)
    reg_ERB = models.IntegerField(default=0)
    reg_1aGIB =models.IntegerField(default=0)
    reg_pubs = models.IntegerField(default=0)
    reg_BAS = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    date = models.CharField(max_length=12)
    def __str__(self):
        return f"61e brought: {self.reg_61e} out of {self.total}"
        
