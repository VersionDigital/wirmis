from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Client(models.Model):

    class Meta:
        ordering = ('name',)


    name = models.CharField(max_length=255)
    email = models.CharField(max_length=128, null=True, blank=True)
    vat = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return u"{}".format(self.name)


class Content(models.Model):
    title = models.CharField(max_length=1023)
    synopsis = models.TextField(null=True, blank=True)

    def __str__(self):
        return u"{}".format(self.title)



BOOKING_STATUS = (
    ('pe', _(u"Pending")),
    ('co', _(u"Confirmed")),
    ('ca', _(u"Cancelled")),
)
BOOKING_STATUS_DICT = {k: v for k, v in BOOKING_STATUS}

class Booking(models.Model):
    content = models.ForeignKey(Content)
    client = models.ForeignKey(Client)
    date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=32, choices=BOOKING_STATUS, default='pending')

    def __str__(self):
        __date = self.date.ctime() if self.date else ""
        return u"{} - {} :: {}".format(__date,
                                         self.content,
                                         self.client)
