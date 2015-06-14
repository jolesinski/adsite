from django.contrib import admin

# Register your models here.
from adverts.models import Advert


class AdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'has_expired')
    list_filter = ['pub_date']

admin.site.register(Advert, AdvertAdmin)