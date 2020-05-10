from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ServiceListView, ServiceUpdateView
from .views import CustomerListView, CustomerDetailsView

urlpatterns=[
    url(r'^customer/$', CustomerListView.as_view(), name='customer'),
    url(r'^customer/(?P<pk>[0-9]+)/$', CustomerDetailsView.as_view(), name='customer-update'),
    url(r'^service/$', ServiceListView.as_view(), name='service'),
    url(r'^service/(?P<pk>[0-9]+)/$', ServiceUpdateView.as_view(), name='service-update'),
]

urlpatterns= format_suffix_patterns(urlpatterns)
