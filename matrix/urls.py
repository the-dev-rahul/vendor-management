from django.urls import path

from .views import PerformanceAPIView


urlpatterns = [
    path('<uuid:vendor_code>/performance', PerformanceAPIView.as_view(), name='performance-api')
]   