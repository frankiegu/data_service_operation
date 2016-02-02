#coding=utf8
import xadmin

from models import Service_category, Service_type,\
    Service_provider, Service_protocol, Service_status, Service_base,\
    Service_reqField, Service_respField, Service_reqDemo, Service_respDemo,\
    Service_api, Service_errorType, Service_errorCode, Service_statistics,\
    Service_contact, Service_tag, Service_invokeDemo, Common_httpDemo,\
    Service_upgrade, Service_others, Service_price, Service_activePack,\
    Service_sdkPack

class ServeCateAdmin(object):
    exclude = ('id',)
xadmin.site.register(Service_category,ServeCateAdmin)

class ServeTypeAdmin(object):
#显示列
    list_display = ('category', 'type_name', 'create_time', 'order_num')
#列表搜索栏
    search_fields = ('type_name',)
#复选框搜索
    #filter_horizontal = ('category',)
    ordering = ('id', 'order_num')
xadmin.site.register(Service_type, ServeTypeAdmin)

class ServeProviderAdmin(object):
    relfield_style = 'fk-ajax'
    search_fields = ['provider_name']
    reversion_enable = True
xadmin.site.register(Service_provider,ServeProviderAdmin)

class ServeProtocolAdmin(object):
    list_display = ('protocol_name', 'support_method')
xadmin.site.register(Service_protocol, ServeProtocolAdmin)

xadmin.site.register(Service_status)

class ServiceBaseAdmin(object):
    list_display = ('serve_name', 'serve_type', 'protocol', 'provider','status')
    search_fields = ('serve_name',)
    relfield_style = 'fk-ajax'
    ordering = ('serve_type', 'id')
    reversion_enable = True
xadmin.site.register(Service_base, ServiceBaseAdmin)

class ServiceReqFieldAdmin(object):
    list_display = ('service', 'field_name', 'field_type', 'required', 'description', 'create_time')
    search_fields = ('service__serve_name',)
#文本框搜索
    raw_id_fields = ('service',)
xadmin.site.register(Service_reqField, ServiceReqFieldAdmin)
 
class ServiceRespFieldAdmin(object):
    list_display = ('service', 'field_name', 'field_type', 'description', 'create_time')
    search_fields = ('service__serve_name',)
    raw_id_fields = ('service',)
xadmin.site.register(Service_respField, ServiceRespFieldAdmin)

class ServiceReqDemoAdmin(object):
    list_display = ('service', 'demo_format', 'demo_str', 'create_time')
    search_fields = ('service__serve_name',)
    raw_id_fields = ('service',)
xadmin.site.register(Service_reqDemo, ServiceReqDemoAdmin)

class ServiceRespDemoAdmin(object):
    list_display = ('service', 'demo_format', 'demo_str', 'create_time')
    search_fields = ('service__serve_name',)
    raw_id_fields = ('service',)
xadmin.site.register(Service_respDemo, ServiceRespDemoAdmin)

class ServiceApiAdmin(object):
    list_display = ('service', 'format', 'url', 'create_time')
    search_fields = ['service__serve_name',]
    raw_id_fields = ('service',)
xadmin.site.register(Service_api, ServiceApiAdmin)

xadmin.site.register(Service_errorType)

class ServiceErrorCodeAdmin(object):
    list_display = ('service', 'error_type', 'error_code', 'error_name', 'create_time')
    search_fields = ('service__serve_name',)
    raw_id_fields = ('service',)
xadmin.site.register(Service_errorCode, ServiceErrorCodeAdmin)

class ServiceStatisticsAdmin(object):
    list_display = ('service', 'scores', 'app_counts','invoke_counts','scan_counts')
    search_fields = ('service__serve_name',)
    raw_id_fields = ('service',)
xadmin.site.register(Service_statistics, ServiceStatisticsAdmin)

class ServiceContactAdmin(object):
    list_display = ('service', 'support_team','support_telno','contactQQ',)
    search_fields = ('service__serve_name',)
    raw_id_fields = ('service',)
xadmin.site.register(Service_contact, ServiceContactAdmin)

xadmin.site.register(Service_tag)

class ServiceInvokeDemoAdmin(object):
    list_display = ('service', 'language', 'title', 'hyperlink', 'provider', 'create_time')
    search_fields = ('service__serve_name',)
    raw_id_fields = ('service',)
xadmin.site.register(Service_invokeDemo, ServiceInvokeDemoAdmin)

class CommonHttpDemoAdmin(object):
    list_display = ('language', 'title', 'hyperlink', 'create_time')
xadmin.site.register(Common_httpDemo, CommonHttpDemoAdmin)

class ServiceUpgradeAdmin(object):
    list_display = ('service', 'upgrade_contents', 'upgrade_time',)
xadmin.site.register(Service_upgrade,ServiceUpgradeAdmin)

class ServiceOthersAdmin(object):
    list_display = ('service', 'title', 'content', 'detail', 'create_time')
    search_fields = ('service__serve_name',)
    raw_id_fields = ('service',)
xadmin.site.register(Service_others, ServiceOthersAdmin)

class ServicePriceAdmin(object):
    list_display = ('service', 'is_free', 'free_times_per', 'per_unit', 'cost', 'create_time')
    search_fields = ('service__serve_name',)
    raw_id_fields = ('service',)
xadmin.site.register(Service_price, ServicePriceAdmin)

class ServiceActivePackAdmin(object):
    list_display = ('service', 'pack_name', 'pack_price', 'by_counts_or_time', 'pack_counts', 'pack_effective_time', 'create_time','status')
    search_fields = ('service__serve_name',)
    raw_id_fields = ('service',)
xadmin.site.register(Service_activePack, ServiceActivePackAdmin)

class ServiceSdkPackAdmin(object):
    list_display = ('service', 'pack_name', 'free_times_per', 'per_unit', 'single_client_free_times_per', 'single_client_per_unit', 'create_time')
    search_fields = ('service__serve_name',)
    raw_id_fields = ('service',)
xadmin.site.register(Service_sdkPack, ServiceSdkPackAdmin)
