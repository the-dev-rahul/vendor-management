from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.functions import Cast
from django.db.models import Count, Q, F, FloatField, ExpressionWrapper, Avg, DurationField
from django.utils import timezone

from .models import PurchaseOrder, PurchaseOrderStatus
from matrix.models import Matrix


@receiver(post_save, sender=PurchaseOrder) 
def matrix_calculation(sender, instance, created, **kwargs):
        
        po_dict = PurchaseOrder.objects.values('vendor').annotate(
                delivered_po=Count('po_number', filter=Q(delivery_date__lt= timezone.now(), vendor=instance.vendor)),
                completed_count=Count('po_number', filter=Q(status = PurchaseOrderStatus.COMPLETED, vendor=instance.vendor)),
                total_count=Count('po_number', filter=Q(vendor=instance.vendor)),
                response_time = F('acknowledgment_date')-F('order_date'),   
                ).filter(
                    vendor=instance.vendor
                ).aggregate(
                        
                    fullfillment_rate=Cast('completed_count', FloatField()) / Cast('total_count', FloatField()),
                    avg_response_time=Avg( ExpressionWrapper(
                                    Cast('response_time', output_field=DurationField()) / 1000000,
                                    output_field=FloatField()
                                    ),
                    ),
                    avg_quality_rating=Avg('quality_rating'),
                    on_time_delivery_rate=Cast('delivered_po', FloatField()) / Cast('completed_count', FloatField())
            )
        
        vendor = instance.vendor
        vendor.on_time_delivery_rate =  po_dict.get('on_time_delivery_rate') if po_dict.get('on_time_delivery_rate') else 0.0
        vendor.quality_rating_avg =   po_dict.get('quality_rating_avg') if po_dict.get('quality_rating_avg') else 0.0
        vendor.average_response_time =   po_dict.get('average_response_time') if po_dict.get('average_response_time') else 0.0
        vendor.fulfillment_rate = po_dict.get('fullfillment_rate') if po_dict.get('fullfillment_rate') else 0.0 
        vendor.save()

        Matrix.objects.create(
            vendor=vendor,
            on_time_delivery_rate = vendor.on_time_delivery_rate,
            quality_rating_avg = vendor.quality_rating_avg,
            average_response_time = vendor.average_response_time,
            fulfillment_rate = vendor.fulfillment_rate
        )