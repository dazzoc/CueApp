from django.contrib import admin
from .models import Album, Listening, Device

# Register your models here.
admin.site.register(Album)
admin.site.register(Listening)
admin.site.register(Device)