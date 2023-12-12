from django.contrib import admin

from .models import Finch, Feeding, Accessory

admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Accessory)

