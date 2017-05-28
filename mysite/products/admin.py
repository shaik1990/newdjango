from django.contrib import admin

from django.db import models
from models import AuditStatus,DeviceType,Model,Hosts,Product,Site,Vendor,AuditData,AuditDummyData
from admin_display_fields_settings.admin import DisplayFieldsSettingsAdmin
#from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter



class VendorAdmin(admin.ModelAdmin):
    list_display=['vendor_name','deleted','date_created']
    list_display_links=('vendor_name',)
    date_hierarchy = 'date_created'
    ordering = ('vendor_id',)
admin.site.register(Vendor,VendorAdmin)

class SiteAdmin(admin.ModelAdmin):
    list_display = ('site_name','site_type', 'deleted', 'date_created','date_updated')
    list_display_links=('site_name',)
    date_hierarchy = 'date_updated'
    ordering = ('site_id','site_type')
admin.site.register(Site,SiteAdmin)


class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('device_type_name', 'deleted', 'date_created','date_updated')
    list_display_links=('device_type_name',)
    date_hierarchy = 'date_created'
    ordering = ('device_type_id','-date_updated','-date_created')
admin.site.register(DeviceType,DeviceTypeAdmin)


class DmodelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'deleted', 'date_created')
    list_display_links=('model_name',)
    date_hierarchy = 'date_created'
    ordering = ('model_id',)
admin.site.register(Model,DmodelAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'deleted', 'date_created')
    list_display_links=('product_name',)
    date_hierarchy = 'date_created'
    ordering = ('product_id',)
admin.site.register(Product,ProductAdmin)


class AuditStatusAdmin(admin.ModelAdmin):
    list_display = ('status_name', 'deleted', 'date_created','date_updated')
    list_display_links=('status_name',)
    date_hierarchy = 'date_created'
    ordering = ('status_id','-date_updated')
admin.site.register(AuditStatus,AuditStatusAdmin)


class HostsAdmin(admin.ModelAdmin):   #DisplayFieldsSettingsAdmin):
    #list_display=[i.name for i in Hosts._meta.fields]
    list_display = ('host_name','ip_address','site_id','vendor_id','model_id','device_type_id', 'deleted', 'date_created','date_updated') 
    list_display_links=('host_name',)
    list_filter = ('device_type_id__device_type_name','site_id__site_name','vendor_id__vendor_name')
    search_fields = ('host_name','device_type_id__device_type_name','vendor_id__vendor_name')
    raw_id_fields = ('site_id',)
    ordering = ('host_id',)
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('host_name',) #'field2','field3'
        return self.readonly_fields
    #prepopulated_fields = {'host_id':('host_name',)}

admin.site.register(Hosts,HostsAdmin)

class AuditDataAdmin(admin.ModelAdmin):
    list_display = [i.name for i in AuditData._meta.fields[1:]] 
    list_display_links=('host_name',)
    # list_filter=(
    # ('product_id',RelatedDropdownFilter),
    # )
    #search_fields = ('host_name','product_id__product_name')
    #list_display = ('host_name', 'config_validation', 'config_validation_review', 'template_creation', 'cms',
    #'remediation','monitoring','global_server_config','server_port','healthcheck',
    #'real_server','virtual_server','service_group','server_vip_group','config_sync',
    #'service','logging_local','logging_remote','username','aaa','nat','match_list',
    #'control_plane','ip_host','ssh','spanning_tree','access_list','prefix_list',
    #'vlan','interfaces','default_gateway','static_routes','ospf','bgp','route_map',
    #'route_policy','as_path_set','community','snmp','accounting_authorization',
    #'tacacs','banner','line_con','monitor','ntp','gre','not_started_field','in_progress',
    #'complete','process_not_started','process_in_progress','process_complete',
    #'not_started','in_progress_nav','in_progress_malt','completed','product_id')
    ordering=('host_id',)            


admin.site.register(AuditData,AuditDataAdmin)
