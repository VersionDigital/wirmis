from django.db import models
from django.utils.translation import ugettext_lazy as _

#from boola.models import Content

class Disk(models.Model):
    name = models.CharField(max_length=8)
    in_transit = models.BooleanField(_(u"out of office?"), default=False)
    # content = models.ForeignKey(Content)

    def __str__(self):
        return "{}".format(self.name)
