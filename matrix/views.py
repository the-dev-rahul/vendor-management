from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializers import PerformanceSerializer
from .models import Matrix


class PerformanceAPIView(ListAPIView):

    queryset = Matrix.objects.filter()
    serializer_class = PerformanceSerializer
    lookup_field = 'vendor_code'

    def get_queryset(self):
        return super().get_queryset().filter(vendor__vendor_code=self.kwargs.get(self.lookup_field, None))