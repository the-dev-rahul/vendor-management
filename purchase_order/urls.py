from django.urls import path

from .views import PurchaseOrderViewSet, AcknowledgePurchaseOrder

urlpatterns = [
    path('', PurchaseOrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='vendor'),
    path('<uuid:po_number>/', PurchaseOrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='vendor'),
    path('<uuid:po_number>/acknowledge', AcknowledgePurchaseOrder.as_view(), name='acknowledge_po'),
]