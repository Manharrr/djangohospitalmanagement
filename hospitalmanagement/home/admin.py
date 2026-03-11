from django.contrib import admin
from .models import Departments,Doctors,Booking

# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)
class Bookingadmin(admin.ModelAdmin):
    list_display=('id','pname','pphone','eemail','docname','bookingdate','bookedon')

admin.site.register(Booking,Bookingadmin)#pass cheyyanam
