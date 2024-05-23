from django.db import models
from utilities import unique_id_model
# Create your models here.

class Vendor(models.Model):

    vendor_code =  unique_id_model()
    name =  models.CharField(max_length=200)
    contact_details =  models.TextField()
    address =  models.TextField()
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg  = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)


    def __str__(self):
        return f'{self.name}-{self.vendor_code}'