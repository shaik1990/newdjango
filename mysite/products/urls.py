from django.conf.urls import url
from django.contrib.auth import views

from views import AuditDataHandler



urlpatterns = [
    #url(r'^gethosts/', HostsHandler, name='HostsHandler'),
    url(r'auditdataget/', AuditDataHandler, name='AuditDataHandler'),
    #url(r'^auditdatasearch/', AuditDataSearchHandler, name='AuditDataSearchHandler'),
]
