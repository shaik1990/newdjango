from rest_framework import serializers
from models import AuditData

class AuditDataSerializer(serializers.HyperlinkedModelSerializer):
    config_validation=serializers.HyperlinkedRelatedField(many=True,view_name='config_validation',source='config_validation.status_name',read_only=True)
    config_validation_review=serializers.HyperlinkedRelatedField(many=True,view_name='config_validation_review',read_only=True)
    template_creation=serializers.HyperlinkedRelatedField(many=True,view_name='template_creation',read_only=True)
    cms=serializers.HyperlinkedRelatedField(many=True,view_name='cms',read_only=True)
    remediation =serializers.HyperlinkedRelatedField(many=True,view_name='remediation',read_only=True)
    Monitoring =serializers.HyperlinkedRelatedField(many=True,view_name='monitoring',read_only=True)
    global_server_config =serializers.HyperlinkedRelatedField(many=True,view_name='global_server_config',read_only=True)
    server_port =serializers.HyperlinkedRelatedField(many=True,view_name='server_port',read_only=True)
    healthcheck =serializers.HyperlinkedRelatedField(many=True,view_name='healthcheck',read_only=True)
    real_server=serializers.HyperlinkedRelatedField(many=True,view_name='real_server',read_only=True)
    virtual_server =serializers.HyperlinkedRelatedField(many=True,view_name='virtual_server',read_only=True)
    service_group =serializers.HyperlinkedRelatedField(many=True,view_name='service_group',read_only=True)
    server_vip_group =serializers.HyperlinkedRelatedField(many=True,view_name='service_vip_group',read_only=True)
    config_sync =serializers.HyperlinkedRelatedField(many=True,view_name='config_sync',read_only=True)
    service =serializers.HyperlinkedRelatedField(many=True,view_name='service',read_only=True)
    logging_local =serializers.HyperlinkedRelatedField(many=True,view_name='logging_local',read_only=True)
    logging_remote=serializers.HyperlinkedRelatedField(many=True,view_name='logging_remote',read_only=True)
    username=serializers.HyperlinkedRelatedField(many=True,view_name='username',read_only=True)
    aaa=serializers.HyperlinkedRelatedField(many=True,view_name='aaa',read_only=True)
    nat=serializers.HyperlinkedRelatedField(many=True,view_name='nat',read_only=True)
    match_list =serializers.HyperlinkedRelatedField(many=True,view_name='match_list',read_only=True)
    control_plane =serializers.HyperlinkedRelatedField(many=True,view_name='control_plane',read_only=True)
    ip_host =serializers.HyperlinkedRelatedField(many=True,view_name='ip_host',read_only=True)
    ssh =serializers.HyperlinkedRelatedField(many=True,view_name='ssh',read_only=True)
    spanning_tree =serializers.HyperlinkedRelatedField(many=True,view_name='spanning_tree',read_only=True)
    access_list =serializers.HyperlinkedRelatedField(many=True,view_name='access_list',read_only=True)
    prefix_list =serializers.HyperlinkedRelatedField(many=True,view_name='prefix_list',read_only=True)
    vlan =serializers.HyperlinkedRelatedField(many=True,view_name='vlan',read_only=True)
    interfaces =serializers.HyperlinkedRelatedField(many=True,view_name='interfaces',read_only=True)
    default_gateway =serializers.HyperlinkedRelatedField(many=True,view_name='default_gateway',read_only=True)
    static_routes =serializers.HyperlinkedRelatedField(many=True,view_name='static_routes',read_only=True)
    ospf =serializers.HyperlinkedRelatedField(many=True,view_name='ospf',read_only=True)
    bgp =serializers.HyperlinkedRelatedField(many=True,view_name='bgp',read_only=True)
    route_map =serializers.HyperlinkedRelatedField(many=True,view_name='route_map',read_only=True)
    route_policy =serializers.HyperlinkedRelatedField(many=True,view_name='route_policy',read_only=True)
    as_path_set =serializers.HyperlinkedRelatedField(many=True,view_name='as_path_set',read_only=True)
    community =serializers.HyperlinkedRelatedField(many=True,view_name='community',read_only=True)
    snmp =serializers.HyperlinkedRelatedField(many=True,view_name='snmp',read_only=True)
    accounting_authorization =serializers.HyperlinkedRelatedField(many=True,view_name='accounting_authorization',read_only=True)
    tacacs =serializers.HyperlinkedRelatedField(many=True,view_name='tacacs',read_only=True)
    banner =serializers.HyperlinkedRelatedField(many=True,view_name='banner',read_only=True)
    line_con =serializers.HyperlinkedRelatedField(many=True,view_name='line_con',read_only=True)
    monitor =serializers.HyperlinkedRelatedField(many=True,view_name='monitor',read_only=True)
    ntp =serializers.HyperlinkedRelatedField(many=True,view_name='ntp',read_only=True)
    gre =serializers.HyperlinkedRelatedField(many=True,view_name='gre',read_only=True)
    product_id=serializers.HyperlinkedRelatedField(many=True,view_name='product_id',read_only=True)

    
    class Meta:
        model=AuditData
        fields=('host_name','config_validation','config_validation_review','template_creation','cms','remediation','Monitoring','global_server_config','server_port','healthcheck','\
        real_server','virtual_server','service_group','server_vip_group','config_sync','\
        service','logging_local','logging_remote','username','aaa','nat','match_list','\
        control_plane','ip_host','ssh','spanning_tree','access_list','prefix_list','\
        vlan','interfaces','default_gateway','static_routes','ospf','bgp','route_map','\
        route_policy','as_path_set','community','snmp','accounting/authorization','\
        tacacs','banner','line_con','monitor','ntp','gre','Not_Started_','In_Progress','\
        Complete','Process_Not_Started','Process_In_Progress','Process_Complete','\
        Not_Started','In_Progress_NAV','In_Progress_MALT','Completed','product_id')



