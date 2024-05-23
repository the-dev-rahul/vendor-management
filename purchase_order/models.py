
import datetime
from django.db  import models
from utilities import unique_id_model
from django.utils import timezone


class PurchaseOrderStatus:

    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

    STATUS_CHOICES = (
        (PENDING, "pending"),
        (COMPLETED, "completed"),
        (CANCELED, "canceled"),
    )


def add_two_days():

    return timezone.now() + timezone.timedelta(days=2)


class PurchaseOrder(models.Model):

    po_number = unique_id_model()
    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(default=add_two_days)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=9, choices=PurchaseOrderStatus.STATUS_CHOICES, default=PurchaseOrderStatus.PENDING)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(null=True)
    acknowledgment_date = models.DateTimeField(null=True)
