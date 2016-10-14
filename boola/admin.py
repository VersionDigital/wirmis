from django.contrib import admin

from boola.models import Client, Content, Booking


class BookingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client)
admin.site.register(Content)
admin.site.register(Booking, BookingAdmin)

