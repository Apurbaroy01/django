from django.contrib import admin
from .models import Product
from import_export.admin import ImportExportModelAdmin


@admin.register(Product)
class DeviceAdmin(ImportExportModelAdmin):
    list_display = ('serial_number', 'product_name', 'product_name', 'mobile_number', 'price', 'product_model_number', 'warranty_date', 'expiry_date', 'created_at')
    search_fields = ('serial_number', 'product_name', 'product_name', 'mobile_number', 'product_model_number')
    list_filter = ('warranty_date', 'expiry_date', 'created_at')
    readonly_fields = ('created_at',)
