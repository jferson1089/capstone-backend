from django.db import models

# Create your models here.

class Customer(models.Model):

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=10)
    vin_number=models.CharField(max_length=17)
    description = models.TextField
    date_created=models.DateTimeField(auto_now_add=True)
    date_requested=models.DateTimeField()

    class Meta:
        verbose_name= 'Customer'
        verbose_name_plural= 'Customers'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField
    avg_time = models.IntegerField
    price = models.IntegerField

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name


