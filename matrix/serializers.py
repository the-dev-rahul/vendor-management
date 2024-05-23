from rest_framework.serializers import ModelSerializer
from .models import Matrix

class PerformanceSerializer(ModelSerializer):

    class Meta:
        model = Matrix
        fields = '__all__'