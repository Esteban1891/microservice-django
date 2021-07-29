from django.contrib import admin
from .models import Direcciones
# Register your models here.
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.

@admin.register(Direcciones)
class ImportViewAdmin(ImportExportActionModelAdmin):
    pass

