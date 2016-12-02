# _*_ coding: utf-8 _*_
from django.db import models
from django.utils.translation import ugettext_lazy as _

#from boola.models import Content, Client
from boola.models import Booking


class Disk(models.Model):

    class Meta:
        ordering = ('name',)


    name = models.CharField(max_length=8)
    in_transit = models.BooleanField(_(u"out of office?"), default=False)
    capacity = models.PositiveIntegerField(null=True, blank=True)

    def sent_to(self):
        if self.in_transit:
            dispatch = Dispatch.objects.filter(disk=self.id).first()
            if dispatch:
                return dispatch.booking.client.name
        return ""

    def __str__(self):
        return "{}".format(self.name)


class Dispatch(models.Model):
    date = models.DateField()
    disk = models.ForeignKey(Disk)
    booking = models.ForeignKey(Booking)

    def __str__(self):
        return "{} - {} - {}".format(self.date,
                                     self.disk.name,
                                     self.booking.client.name
                                     )
