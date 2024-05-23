from django.urls import path

from .views import VendorViewSet

urlpatterns = [
    path('', VendorViewSet.as_view({'get': 'list', 'post': 'create'}), name='vendor'),
    path('<uuid:vendor_code>/', VendorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='vendor'),
]