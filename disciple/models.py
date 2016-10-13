from django.db import models

class Disk(models.Model):
    name = models.CharField(max_length=8)
