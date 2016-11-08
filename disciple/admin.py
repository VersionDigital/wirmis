#from django import forms
from django.contrib import admin
#from django.contrib.admin.filters import SimpleListFilter

from disciple.models import Disk, Dispatch

class DiskAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'in_transit',)
    search_fields = ('content__title',)
    list_filter = ('content__title', 'in_transit',)


class DispatchAdmin(admin.ModelAdmin):
    search_fields = ('disk__content__title', 'client__name', 'disk__name')


admin.site.register(Disk, DiskAdmin)
admin.site.register(Dispatch, DispatchAdmin)
