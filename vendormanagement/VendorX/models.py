from django.db import models


class VendorModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    contact_details = models.TextField(max_length=100, null=False)
    address = models.TextField(max_length=200, null=False)
    vendor_code = models.AutoField(primary_key=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fullfillment_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.vendor_code, self.name, self.contact_details, self.address, \
            self.on_time_delivery_rate, self.average_response_time, self.fullfillment_rate


class PurchaseOrder(models.Model):
    po_number = models.CharField(primary_key=True, max_length=200)
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField(null=False)
    quantity = models.IntegerField(null=False)
    status = models.CharField(null=False, max_length=200)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(null=True, blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number, self.vendor, self.order_date, self.delivery_date, \
            self.items, self.quantity, self.status, self.quality_rating, self.issue_date, self.acknowledgment_date


class PerformanceModel(models.Model):
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.vendor, self.date, self.on_time_delivery_rate, self.quality_rating_avg, \
            self.average_response_time, self.fulfillment_rate
