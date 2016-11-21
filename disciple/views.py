# _*_ coding: utf-8 _*_
# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from disciple.models import Disk, Dispatch

# Create your views here.

class DiskListView(ListView):

    model = Disk
    template_name = "disks.html"

    def get_context_data(self, **kwargs):
        context = super(DiskListView, self).get_context_data(**kwargs)
        print(">>>>>> %s" % context)
        return context


class DiskCreate(CreateView):
    model = Disk
    template_name = "create_disk.html"

    fields = ['name', 'content', 'capacity', ]

class DispatchListView(ListView):

    model = Dispatch
    template_name = "dispatches.html"

    def get_context_data(self, **kw):
        context = super(DispatchListView, self).get_context_data(**kw)
        return context
