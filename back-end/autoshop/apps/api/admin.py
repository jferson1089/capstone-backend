from django.contrib import admin
from apps.api.models import Customer
from apps.api.models import Service

# Register your models here.

admin.site.register(Customer)
admin.site.register(Service)