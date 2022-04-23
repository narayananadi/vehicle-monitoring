from django.contrib import admin
from . models import numplate_checkin_data, numplate_checkout_data

admin.site.register(numplate_checkin_data)
admin.site.register(numplate_checkout_data)

# Register your models here.
