import rest_framework_filters as filters
from models import Service_category, Service_type, Service_base, Service_statistics,Service_api,\
    Service_respField, Service_respDemo,Service_reqDemo, Service_reqField, Service_errorCode,\
    Service_sdkPack, Service_price, Service_activePack, Service_invokeDemo, Service_upgrade, Service_contact


class ServiceCategoryFilter(filters.FilterSet):
    category_name = filters.AllLookupsFilter(name="category_name")
    crt_time_after = filters.DateFilter(name="create_time", lookup_type='gte')
    class Meta:
        model = Service_category
        fields = ['id', 'category_name', 'cate_abbreviation', 'crt_time_after',]
#    filter_fields = {
#                  'category_name': ['exact', 'icontains'],
#                  'id': ['exact', 'gte', 'lte'],
#                }

class ServiceTypeFilter(filters.FilterSet):
    type_name = filters.AllLookupsFilter(name="type_name")
    category = filters.RelatedFilter(ServiceCategoryFilter,name='category')
    class Meta:
        model = Service_type
        fields = ['id', 'type_name', 'type_abbreviation', 'category',]

class ServiceBaseFilter(filters.FilterSet):
    id = filters.AllLookupsFilter(name="id")
    serve_name = filters.AllLookupsFilter(name="serve_name")
    serve_type = filters.RelatedFilter(ServiceTypeFilter,name='serve_type')
    type_id = filters.NumberFilter(name="serve_type__id")
    category_id = filters.NumberFilter(name="serve_type__category")
    class Meta:
        model = Service_base
        fields = ['id', 'serve_name', 'serve_abbreviation', 'serve_type', 'category_id', 'type_id']

class ServiceStatisticsFilter(filters.FilterSet):
    service = filters.RelatedFilter(ServiceBaseFilter,name='service')
    class Meta:
        model = Service_statistics
        fields = ['id', 'service', 'scores', 'app_counts', 'invoke_counts', 'scan_counts',]

class ServiceAPISecretFilter(filters.FilterSet):
    service = filters.RelatedFilter(ServiceBaseFilter,name='service')
    class Meta:
        model = Service_api
        fields = ['id', 'service', 'format', 'create_time', ]

class ServiceAPIFilter(filters.FilterSet):
    class Meta:
        model = Service_api
        fields = ['id', 'service', 'format', 'create_time', ]
        
class ServiceReqDemoFilter(filters.FilterSet):
    class Meta:
        model = Service_reqDemo
        fields = ['id', 'service', 'demo_format', 'create_time', ]
    
class ServiceReqFieldFilter(filters.FilterSet):
    class Meta:
        model = Service_reqField
        fields = ['id', 'service', 'field_name', 'create_time', ]
    
class ServiceRespDemoFilter(filters.FilterSet):
    class Meta:
        model = Service_respDemo
        fields = ['id', 'service', 'demo_format', 'create_time', ]
        
class ServiceRespFieldFilter(filters.FilterSet):
    class Meta:
        model = Service_respField
        fields = ['id', 'service', 'field_name', 'create_time', ]


class ServiceErrorCodeFilter(filters.FilterSet):
    error_type_id = filters.NumberFilter(name='error_type__id')
    error_type_name = filters.NumberFilter(name='error_type__error_type_name')
    class Meta:
        model = Service_errorCode
        fields = ['id', 'service', 'error_type_id', 'error_type_name', 'error_code', 'error_name','create_time', ]


class ServicePriceFilter(filters.FilterSet):
    cost = filters.NumberFilter(name="cost",lookup_type='lte')
    class Meta:
        model = Service_price
        fields = ['id', 'service', 'is_free', 'cost', 'create_time']
    

class ServiceActivePackFilter(filters.FilterSet):
    pack_name = filters.AllLookupsFilter(name="pack_name")
    pack_price = filters.NumberFilter(name="pack_price",lookup_type='lte')
    class Meta:
        model = Service_activePack
        fields = ['id', 'service', 'pack_name', 'pack_price', 'status', 'create_time']


class ServiceSDKPackFilter(filters.FilterSet):
    pack_name = filters.AllLookupsFilter(name="pack_name")
    class Meta:
        model = Service_sdkPack
        fields = ['id', 'service', 'pack_name', 'create_time', ]
        
class ServiceInvokeDemoFilter(filters.FilterSet):
    title = filters.AllLookupsFilter(name="title")
    class Meta:
        model = Service_invokeDemo
        fields = ['id', 'service', 'title', 'language', 'provider', 'create_time', ]
        
class ServiceUpgradeFilter(filters.FilterSet):
    upgrade_title = filters.AllLookupsFilter(name="upgrade_title")
    upgrade_contents = filters.AllLookupsFilter(name="upgrade_contents")
    class Meta:
        model = Service_upgrade
        fields = ['id', 'service', 'upgrade_title', 'upgrade_contents', 'upgrade_time', ]

class ServiceContactFilter(filters.FilterSet):
    class Meta:
        model = Service_contact
        fields = ['id', 'service',]


