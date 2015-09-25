from django.contrib import admin

from .models import Stock, Trader, Viewer

# Register your models here.
admin.site.register(Stock)
admin.site.register(Trader)
admin.site.register(Viewer)
