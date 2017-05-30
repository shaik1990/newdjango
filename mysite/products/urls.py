from django.conf.urls import url
from django.contrib.auth import views
from . import views

from views import AuditDataHandler,AuditDataUpdateHandler,AuditDataDeleteHandler



urlpatterns = [
    #url(r'^gethosts/', HostsHandler, name='HostsHandler'),
    #url(r'^$',views.testviewHandler(),name='testviewHandler'),
    url(r'auditdataget/', AuditDataHandler, name='AuditDataHandler'),
    url(r'^auditdatadelete/', AuditDataDeleteHandler, name='AuditDataDeleteHandler'),
    url(r'^auditdataupdate/', AuditDataUpdateHandler, name='AuditDataUpdateHandler'),
    #url(r'^auditdatasearch/', AuditDataSearchHandler, name='AuditDataSearchHandler'),
]
