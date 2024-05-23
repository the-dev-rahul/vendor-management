from rest_framework.serializers import ModelSerializer

from vendor.models import Vendor 


class VendorSerializer(ModelSerializer):


    class Meta:

        model = Vendor
        fields = '__all__'