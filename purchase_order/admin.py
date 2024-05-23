from django.contrib import admin
from purchase_order.models import PurchaseOrder
# Register your models here.


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display =  ('po_number', 'status', 'vendor',)

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)