from django.db import models
from django.contrib.auth.models import User
from extpack.macaddress.fields import MACAddressField

# Create your models here.
class Devices(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True)
    macAdd = MACAddressField(null=True, blank=True)
    apiKey = models.CharField(max_length=100, unique=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + "-" + self.name