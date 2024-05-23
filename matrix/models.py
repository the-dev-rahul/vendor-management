from django.db import models

# Create your models here.


class Matrix(models.Model):

    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    on_time_delivery_rate =  models.FloatField()
    quality_rating_avg =  models.FloatField()
    average_response_time =  models.FloatField()
    fulfillment_rate =  models.FloatField()