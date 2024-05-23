from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import PurchaseOrder
from .serializers import  PurchaseOrderSerializer, PurchaseOrderListSerializer, AcknowledgePurchaseOrderSerializer
# Create your views here.


class PurchaseOrderViewSet(viewsets.ModelViewSet):

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'po_number'

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return PurchaseOrderSerializer
        return PurchaseOrderListSerializer
    

class AcknowledgePurchaseOrder(UpdateAPIView):

    queryset = PurchaseOrder.objects.all()
    serializer_class = AcknowledgePurchaseOrderSerializer
    lookup_field = 'po_number'