from django.contrib import admin

# Register your models here.
from .models import TemporaryFiles

@admin.register(TemporaryFiles)
class TempFiles(admin.ModelAdmin):
    list_display=['pk','file']
