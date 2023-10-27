from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *



class SessionAdmin(ImportExportModelAdmin):
    list_display = ("id", "sessionNumber","phoneNumber","text","response","date_added")
    pass
admin.site.register(Sessions, SessionAdmin)
