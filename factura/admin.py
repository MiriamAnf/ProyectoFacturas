from django.contrib import admin

from factura.models import Receipt

from factura.models import LineReceipt

class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        'num_receipt',
        'costumer_name',
        'costumer_address',
        'date_of_issue',
    )
    search_fields = ('num_receipt', 'costumer_name')
    date_hierarchy = 'date_of_issue'

admin.site.register(Receipt, ReceiptAdmin)

class LineReceiptAdmin(admin.ModelAdmin):
    list_display = (
        'receipt',
        'id_product',
        'product_name',
        'unit_price',
        'units',
        'base_imponible',
    )

admin.site.register(LineReceipt, LineReceiptAdmin)