from django.contrib import admin
from .models import studentgriev , contactus
# Register your models here.

admin.site.site_header = "Nhitm-SGRC"

class studentgrievAdmin(admin.ModelAdmin):
    list_display = ["name","contactnum","email","grievance","date_time","is_solved"]


admin.site.register(studentgriev,studentgrievAdmin),
admin.site.register(contactus)
