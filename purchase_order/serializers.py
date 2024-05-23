from rest_framework.serializers import ModelSerializer
from django.utils import timezone

from purchase_order.models import PurchaseOrder 



class PurchaseOrderListSerializer(ModelSerializer):

    class Meta:

        model = PurchaseOrder
        fields = '__all__'


class PurchaseOrderSerializer(ModelSerializer):

    class Meta:

        model = PurchaseOrder
        fields = ['po_number', 'vendor', 'items', 'quantity']


class AcknowledgePurchaseOrderSerializer(ModelSerializer):

    class Meta:

        model = PurchaseOrder
        fields = []
    

    def update(self, instance, validated_data):

        validated_data['acknowledgment_date'] = timezone.now()
        return super().update(instance, validated_data)