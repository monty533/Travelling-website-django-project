from django.contrib import admin
from .models import Destination

# Register your models here.
class AdminDestination(admin.ModelAdmin):
    list_display = ['id','name','img','desc','price']

admin.site.register(Destination,AdminDestination)
