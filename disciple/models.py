from django.db import models
from django.utils.translation import ugettext_lazy as _

from boola.models import Content, Client

class Disk(models.Model):
    name = models.CharField(max_length=8)
    in_transit = models.BooleanField(_(u"out of office?"), default=False)
    content = models.ForeignKey(Content, null=True)

    def __str__(self):
        return "{}".format(self.name)

class Dispatch(models.Model):
    date = models.DateField()
    disk = models.ForeignKey(Disk)
    client = models.ForeignKey(Client)
