from django.contrib import admin
from .models import VendorModel, PurchaseOrder, PerformanceModel

admin.site.register(VendorModel)
admin.site.register(PurchaseOrder)
admin.site.register(PerformanceModel)