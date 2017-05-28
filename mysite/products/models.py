# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuditData(models.Model):
    host_id = models.AutoField(primary_key=True)
    host_name = models.ForeignKey('Hosts', related_name='Hosts_host_name', db_column='host_name', )
    config_validation = models.ForeignKey('AuditStatus', related_name='Audit_status_config',
                                          db_column='Config_Validation', blank=True,
                                          null=True)  # Field name made lowercase.
    config_validation_review = models.ForeignKey('AuditStatus', related_name='Audit_status_config_review',
                                                 db_column='Config_Validation_Review', blank=True,
                                                 null=True)  # Field name made lowercase.
    template_creation = models.ForeignKey('AuditStatus', related_name='Audit_status_tempalte_creation',
                                          db_column='Template_Creation', blank=True,
                                          null=True)  # Field name made lowercase.
    cms = models.ForeignKey('AuditStatus', related_name='Audit_status_cms', db_column='CMS', blank=True,
                            null=True)  # Field name made lowercase.
    remediation = models.ForeignKey('AuditStatus', related_name='Audit_status_remediation', db_column='Remediation',
                                    blank=True, null=True)  # Field name made lowercase.
    monitoring = models.ForeignKey('AuditStatus', related_name='Audit_status_monitoring', db_column='Monitoring',
                                   blank=True, null=True)  # Field name made lowercase.
    global_server_config = models.ForeignKey('AuditStatus', related_name='Audit_status_global_server_config',
                                             db_column='Global_Server_Config', blank=True,
                                             null=True)  # Field name made lowercase.
    server_port = models.ForeignKey('AuditStatus', related_name='Audit_status_server_port', db_column='Server_Port',
                                    blank=True, null=True)  # Field name made lowercase.
    healthcheck = models.ForeignKey('AuditStatus', related_name='Audit_status_healthcheck', db_column='Healthcheck',
                                    blank=True, null=True)  # Field name made lowercase.
    real_server = models.ForeignKey('AuditStatus', related_name='Audit_status_Real_server', db_column='Real_Server',
                                    blank=True, null=True)  # Field name made lowercase.
    virtual_server = models.ForeignKey('AuditStatus', related_name='Audit_status_Virtual_server',
                                       db_column='Virtual_Server', blank=True, null=True)  # Field name made lowercase.
    service_group = models.ForeignKey('AuditStatus', related_name='Audit_status_Service_group',
                                      db_column='Service_Group', blank=True, null=True)  # Field name made lowercase.
    server_vip_group = models.ForeignKey('AuditStatus', related_name='Audit_status_Server_vip_group',
                                         db_column='Server_Vip_Group', blank=True,
                                         null=True)  # Field name made lowercase.
    config_sync = models.ForeignKey('AuditStatus', related_name='Audit_status_config_sync', db_column='Config_Sync',
                                    blank=True, null=True)  # Field name made lowercase.
    service = models.ForeignKey('AuditStatus', related_name='Audit_status_service', db_column='Service', blank=True,
                                null=True)  # Field name made lowercase.
    logging_local = models.ForeignKey('AuditStatus', related_name='Audit_status_logging_local',
                                      db_column='Logging_Local', blank=True, null=True)  # Field name made lowercase.
    logging_remote = models.ForeignKey('AuditStatus', related_name='Audit_status_logging_remote',
                                       db_column='Logging_Remote', blank=True, null=True)  # Field name made lowercase.
    username = models.ForeignKey('AuditStatus', related_name='Audit_status_username', db_column='Username', blank=True,
                                 null=True)  # Field name made lowercase.
    aaa = models.ForeignKey('AuditStatus', related_name='Audit_status_aaa', db_column='Aaa', blank=True,
                            null=True)  # Field name made lowercase.
    nat = models.ForeignKey('AuditStatus', related_name='Audit_status_nat', db_column='Nat', blank=True,
                            null=True)  # Field name made lowercase.
    match_list = models.ForeignKey('AuditStatus', related_name='Audit_status_match_list', db_column='Match_List',
                                   blank=True, null=True)  # Field name made lowercase.
    control_plane = models.ForeignKey('AuditStatus', related_name='Audit_status_control_plane',
                                      db_column='Control_Plane', blank=True, null=True)  # Field name made lowercase.
    ip_host = models.ForeignKey('AuditStatus', related_name='Audit_status_ip_host', db_column='Ip_Host', blank=True,
                                null=True)  # Field name made lowercase.
    ssh = models.ForeignKey('AuditStatus', related_name='Audit_status_ssh', db_column='Ssh', blank=True,
                            null=True)  # Field name made lowercase.
    spanning_tree = models.ForeignKey('AuditStatus', related_name='Audit_status_spanning_tree',
                                      db_column='Spanning_Tree', blank=True, null=True)  # Field name made lowercase.
    access_list = models.ForeignKey('AuditStatus', related_name='Audit_status_access_list', db_column='Access_List',
                                    blank=True, null=True)  # Field name made lowercase.
    prefix_list = models.ForeignKey('AuditStatus', related_name='Audit_status_prefix_list', db_column='Prefix_List',
                                    blank=True, null=True)  # Field name made lowercase.
    vlan = models.ForeignKey('AuditStatus', related_name='Audit_status_vlan', db_column='Vlan', blank=True,
                             null=True)  # Field name made lowercase.
    interfaces = models.ForeignKey('AuditStatus', related_name='Audit_status_interfaces', db_column='Interfaces',
                                   blank=True, null=True)  # Field name made lowercase.
    default_gateway = models.ForeignKey('AuditStatus', related_name='Audit_status_default_gateway',
                                        db_column='Default_Gateway', blank=True,
                                        null=True)  # Field name made lowercase.
    static_routes = models.ForeignKey('AuditStatus', related_name='Audit_status_static_routes',
                                      db_column='Static_Routes', blank=True, null=True)  # Field name made lowercase.
    ospf = models.ForeignKey('AuditStatus', related_name='Audit_status_ospf', db_column='Ospf', blank=True,
                             null=True)  # Field name made lowercase.
    bgp = models.ForeignKey('AuditStatus', related_name='Audit_status_bgp', db_column='Bgp', blank=True,
                            null=True)  # Field name made lowercase.
    route_map = models.ForeignKey('AuditStatus', related_name='Audit_status_route_map', db_column='Route_Map',
                                  blank=True, null=True)  # Field name made lowercase.
    route_policy = models.ForeignKey('AuditStatus', related_name='Audit_status_route_policy', db_column='Route_Policy',
                                     blank=True, null=True)  # Field name made lowercase.
    as_path_set = models.ForeignKey('AuditStatus', related_name='Audit_status_as_path_set', db_column='As_Path_Set',
                                    blank=True, null=True)  # Field name made lowercase.
    community = models.ForeignKey('AuditStatus', related_name='Audit_status_community', db_column='Community',
                                  blank=True, null=True)  # Field name made lowercase.
    snmp = models.ForeignKey('AuditStatus', related_name='Audit_status_snmp', db_column='Snmp', blank=True,
                             null=True)  # Field name made lowercase.
    accounting_authorization = models.ForeignKey('AuditStatus', related_name='Audit_status_accounting_authorization',
                                                 db_column='Accounting_Authorization', blank=True,
                                                 null=True)  # Field name made lowercase.
    tacacs = models.ForeignKey('AuditStatus', related_name='Audit_status_tacacs', db_column='Tacacs', blank=True,
                               null=True)  # Field name made lowercase.
    banner = models.ForeignKey('AuditStatus', related_name='Audit_status_banner', db_column='Banner', blank=True,
                               null=True)  # Field name made lowercase.
    line_con = models.ForeignKey('AuditStatus', related_name='Audit_status_line_con', db_column='Line_Con', blank=True,
                                 null=True)  # Field name made lowercase.
    monitor = models.ForeignKey('AuditStatus', related_name='Audit_status_monitor', db_column='Monitor', blank=True,
                                null=True)  # Field name made lowercase.
    ntp = models.ForeignKey('AuditStatus', related_name='Audit_status_ntp', db_column='Ntp', blank=True,
                            null=True)  # Field name made lowercase.
    gre = models.ForeignKey('AuditStatus', related_name='Audit_status_gre', db_column='Gre', blank=True,
                            null=True)  # Field name made lowercase.
    not_started_field = models.IntegerField(db_column='Not_Started_', blank=True,
                                            null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    in_progress = models.IntegerField(db_column='In_Progress', blank=True, null=True)  # Field name made lowercase.
    complete = models.IntegerField(db_column='Complete', blank=True, null=True)  # Field name made lowercase.
    process_not_started = models.IntegerField(db_column='Process_Not_Started', blank=True,
                                              null=True)  # Field name made lowercase.
    process_in_progress = models.IntegerField(db_column='Process_In_Progress', blank=True,
                                              null=True)  # Field name made lowercase.
    process_complete = models.IntegerField(db_column='Process_Complete', blank=True,
                                           null=True)  # Field name made lowercase.
    not_started = models.IntegerField(db_column='Not_Started', blank=True, null=True)  # Field name made lowercase.
    in_progress_nav = models.IntegerField(db_column='In_Progress_NAV', blank=True,
                                          null=True)  # Field name made lowercase.
    in_progress_malt = models.IntegerField(db_column='In_Progress_MALT', blank=True,
                                           null=True)  # Field name made lowercase.
    completed = models.IntegerField(db_column='Completed', blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey('Product')

    class Meta:
        managed = False
        db_table = 'audit_data'
        verbose_name_plural = 'Audit Data'


class AuditDummyData(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='Hostname', max_length=45)  # Field name made lowercase.
    device_type = models.CharField(db_column='Device_Type', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=30, blank=True,
                                null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=72)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=75, blank=True, null=True)  # Field name made lowercase.
    config_validation = models.IntegerField(db_column='Config_Validation', blank=True,
                                            null=True)  # Field name made lowercase.
    config_validation_review = models.IntegerField(db_column='Config_Validation_Review', blank=True,
                                                   null=True)  # Field name made lowercase.
    template_creation = models.IntegerField(db_column='Template_Creation', blank=True,
                                            null=True)  # Field name made lowercase.
    cms = models.IntegerField(db_column='CMS', blank=True, null=True)  # Field name made lowercase.
    remediation = models.IntegerField(db_column='Remediation', blank=True, null=True)  # Field name made lowercase.
    monitoring = models.IntegerField(db_column='Monitoring', blank=True, null=True)  # Field name made lowercase.
    global_server_config = models.IntegerField(db_column='Global_Server_Config', blank=True,
                                               null=True)  # Field name made lowercase.
    server_port = models.IntegerField(db_column='Server_Port', blank=True, null=True)  # Field name made lowercase.
    healthcheck = models.IntegerField(db_column='Healthcheck', blank=True, null=True)  # Field name made lowercase.
    real_server = models.IntegerField(db_column='Real_Server', blank=True, null=True)  # Field name made lowercase.
    virtual_server = models.IntegerField(db_column='Virtual_Server', blank=True,
                                         null=True)  # Field name made lowercase.
    service_group = models.IntegerField(db_column='Service_Group', blank=True, null=True)  # Field name made lowercase.
    server_vip_group = models.IntegerField(db_column='Server_Vip_Group', blank=True,
                                           null=True)  # Field name made lowercase.
    config_sync = models.IntegerField(db_column='Config_Sync', blank=True, null=True)  # Field name made lowercase.
    service = models.IntegerField(db_column='Service', blank=True, null=True)  # Field name made lowercase.
    logging_local = models.IntegerField(db_column='Logging_Local', blank=True, null=True)  # Field name made lowercase.
    logging_remote = models.IntegerField(db_column='Logging_Remote', blank=True,
                                         null=True)  # Field name made lowercase.
    username = models.IntegerField(db_column='Username', blank=True, null=True)  # Field name made lowercase.
    aaa = models.IntegerField(db_column='Aaa', blank=True, null=True)  # Field name made lowercase.
    nat = models.IntegerField(db_column='Nat', blank=True, null=True)  # Field name made lowercase.
    match_list = models.IntegerField(db_column='Match_List', blank=True, null=True)  # Field name made lowercase.
    control_plane = models.IntegerField(db_column='Control_Plane', blank=True, null=True)  # Field name made lowercase.
    ip_host = models.IntegerField(db_column='Ip_Host', blank=True, null=True)  # Field name made lowercase.
    ssh = models.IntegerField(db_column='Ssh', blank=True, null=True)  # Field name made lowercase.
    spanning_tree = models.IntegerField(db_column='Spanning_Tree', blank=True, null=True)  # Field name made lowercase.
    access_list = models.IntegerField(db_column='Access_List', blank=True, null=True)  # Field name made lowercase.
    prefix_list = models.IntegerField(db_column='Prefix_List', blank=True, null=True)  # Field name made lowercase.
    vlan = models.IntegerField(db_column='Vlan', blank=True, null=True)  # Field name made lowercase.
    interfaces = models.IntegerField(db_column='Interfaces', blank=True, null=True)  # Field name made lowercase.
    default_gateway = models.IntegerField(db_column='Default_Gateway', blank=True,
                                          null=True)  # Field name made lowercase.
    static_routes = models.IntegerField(db_column='Static_Routes', blank=True, null=True)  # Field name made lowercase.
    ospf = models.IntegerField(db_column='Ospf', blank=True, null=True)  # Field name made lowercase.
    bgp = models.IntegerField(db_column='Bgp', blank=True, null=True)  # Field name made lowercase.
    route_map = models.IntegerField(db_column='Route_Map', blank=True, null=True)  # Field name made lowercase.
    route_policy = models.IntegerField(db_column='Route_Policy', blank=True, null=True)  # Field name made lowercase.
    as_path_set = models.IntegerField(db_column='As_Path_Set', blank=True, null=True)  # Field name made lowercase.
    community = models.IntegerField(db_column='Community', blank=True, null=True)  # Field name made lowercase.
    snmp = models.IntegerField(db_column='Snmp', blank=True, null=True)  # Field name made lowercase.
    accounting_authorization = models.IntegerField(db_column='Accounting_Authorization', blank=True,
                                                   null=True)  # Field name made lowercase.
    tacacs = models.IntegerField(db_column='Tacacs', blank=True, null=True)  # Field name made lowercase.
    banner = models.IntegerField(db_column='Banner', blank=True, null=True)  # Field name made lowercase.
    line_con = models.IntegerField(db_column='Line_Con', blank=True, null=True)  # Field name made lowercase.
    monitor = models.IntegerField(db_column='Monitor', blank=True, null=True)  # Field name made lowercase.
    ntp = models.IntegerField(db_column='Ntp', blank=True, null=True)  # Field name made lowercase.
    gre = models.IntegerField(db_column='Gre', blank=True, null=True)  # Field name made lowercase.
    not_started = models.IntegerField(db_column='Not_Started', blank=True, null=True)  # Field name made lowercase.
    in_progress = models.IntegerField(db_column='In_Progress', blank=True, null=True)  # Field name made lowercase.
    complete = models.IntegerField(db_column='Complete', blank=True, null=True)  # Field name made lowercase.
    process_not_started = models.IntegerField(db_column='Process_Not_Started', blank=True,
                                              null=True)  # Field name made lowercase.
    process_in_progress = models.IntegerField(db_column='Process_In_Progress', blank=True,
                                              null=True)  # Field name made lowercase.
    process_complete = models.IntegerField(db_column='Process_Complete', blank=True,
                                           null=True)  # Field name made lowercase.
    not_started_gray = models.IntegerField(db_column='Not_Started_Gray', blank=True,
                                           null=True)  # Field name made lowercase.
    in_progress_nav = models.IntegerField(db_column='In_Progress_NAV', blank=True,
                                          null=True)  # Field name made lowercase.
    in_progress_malt = models.IntegerField(db_column='In_Progress_MALT', blank=True,
                                           null=True)  # Field name made lowercase.
    complete_gray = models.IntegerField(db_column='Complete_Gray', blank=True, null=True)  # Field name made lowercase.
    adutdatatype = models.IntegerField(db_column='AdutDataType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'audit_dummy_data'


class AuditStatus(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status_name = models.CharField(unique=True, max_length=50)
    deleted = models.IntegerField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audit_status'
        verbose_name_plural = 'Audit Status'

    def __unicode__(self):
        return self.status_name


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DeviceType(models.Model):
    device_type_id = models.AutoField(primary_key=True)
    device_type_name = models.CharField(unique=True, max_length=20)
    deleted = models.IntegerField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'device_type'
        verbose_name_plural = 'Device Type'

    def __unicode__(self):
        return self.device_type_name


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hosts(models.Model):
    host_id = models.AutoField(primary_key=True)
    host_name = models.CharField(primary_key=True, max_length=45)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    site = models.ForeignKey('Site', blank=True, null=True)
    vendor = models.ForeignKey('Vendor', blank=True, null=True)
    model = models.ForeignKey('Model', blank=True, null=True)
    device_type = models.ForeignKey('DeviceType', blank=True, null=True)
    deleted = models.IntegerField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hosts'
        verbose_name_plural = 'hosts'

    def __unicode__(self):
        return self.host_name


class Model(models.Model):
    model_id = models.BigIntegerField(primary_key=True)
    model_name = models.CharField(unique=True, max_length=72)
    deleted = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'model'
        verbose_name_plural = 'model'

    def __unicode__(self):
        return self.model_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(unique=True, max_length=10)
    deleted = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product'
        verbose_name_plural = 'product'

    def __unicode__(self):
        return self.product_name


class Site(models.Model):
    site_id = models.BigIntegerField(primary_key=True)
    site_name = models.CharField(unique=True, max_length=72)
    site_type = models.IntegerField()
    deleted = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'site'
        verbose_name_plural = 'site'

    def __unicode__(self):
        return self.site_name


class Vendor(models.Model):
    vendor_id = models.BigIntegerField(primary_key=True)
    vendor_name = models.CharField(unique=True, max_length=72)
    deleted = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vendor'
        verbose_name_plural = 'vendor'

    def __unicode__(self):
        return self.vendor_name