# _*_ coding: utf-8 _*_

# from django.shortcuts import render
from django.views.generic.list import ListView
from boola.models import Booking

# Create your views here.

class BookingListView(ListView):

    model = Booking
    template_name = "bookings.html"

    def get_context_data(self, **kwargs):
        context = super(BookingListView, self).get_context_data(**kwargs)
        return context
