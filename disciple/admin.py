#from django import forms
from django.contrib import admin
#from django.contrib.admin.filters import SimpleListFilter

from disciple.models import Disk, Dispatch

class DiskAdmin(admin.ModelAdmin):
    list_display = ('name', 'in_transit', 'capacity',)
    list_filter = ('in_transit',)


class DispatchAdmin(admin.ModelAdmin):
    search_fields = ('booking__content__title',
                     'booking__client__name',
                     'disk__name')


admin.site.register(Disk, DiskAdmin)
admin.site.register(Dispatch, DispatchAdmin)

