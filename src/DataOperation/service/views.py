#coding=utf8
from rest_framework import viewsets #@UnresolvedImport

from serializers import ServiceCategorySerializer,\
    ServiceTypeSerializer, ServiceProviderSerializer, ServiceProtocolSerializer,\
    ServiceStatusSerializer, ServiceTagSerializer, ServiceBaseSerializer,\
    ServiceFieldTypeSerializer, ServiceReqFieldSerializer,\
    ServiceRespFieldSerializer, ServiceReqDemoSerializer,\
    ServiceRespDemoSerializer, ServiceApiSerializer, ServiceErrorTypeSerializer,\
    ServiceErrorCodeSerializer, ServiceUpgradeSerializer,\
    ServiceStatisticsSerializer, ServiceContactSerializer,\
    ServiceOthersSerializer, ServiceInvokeDemoSerializer,\
    CommonHttpDemoSerializer, ServicePriceSerializer,\
    ServiceActivePackSerializer, ServiceSdkPackSerializer, Cate_Type_Base_Serializer, ServiceApiSecretSerializer
from models import Service_category, Service_type,\
    Service_provider, Service_protocol, Service_status, Service_tag,\
    Service_base, Service_fieldType, Service_reqField, Service_respField,\
    Service_reqDemo, Service_respDemo, Service_api, Service_errorType,\
    Service_errorCode, Service_upgrade, Service_statistics, Service_contact,\
    Service_others, Service_invokeDemo, Common_httpDemo, Service_price,\
    Service_activePack, Service_sdkPack
#from service.permissions import JustReadOnly #@UnresolvedImport
#from rest_framework.authentication import BasicAuthentication, SessionAuthentication #@UnresolvedImport
from rest_framework import filters 
from filters import ServiceCategoryFilter, ServiceTypeFilter, ServiceBaseFilter , ServiceStatisticsFilter,ServiceAPIFilter,\
    ServiceRespFieldFilter, ServiceReqDemoFilter, ServiceRespDemoFilter, ServiceReqFieldFilter,ServiceErrorCodeFilter,ServicePriceFilter,\
    ServiceActivePackFilter, ServiceSDKPackFilter, ServiceInvokeDemoFilter, ServiceUpgradeFilter, ServiceContactFilter,ServiceAPISecretFilter
from rest_framework.permissions import IsAuthenticated


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = Service_category.objects.all() #@UndefinedVariable
    serializer_class = ServiceCategorySerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
#    filter_fields = ('id','category_name',)
#    filter_fields = {
#                  'category_name': ['exact', 'icontains'],
#                  'id': ['exact', 'gte', 'lte'],
#                }
    filter_class = ServiceCategoryFilter
    ordering_fields = '__all__'
#    def perform_create(self, serializer):
#        serializer.save(owner=self.request.user)
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset


class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = Service_type.objects.all()  #@UndefinedVariable
    serializer_class = ServiceTypeSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceTypeFilter
    ordering_fields = '__all__'
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset


class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = Service_provider.objects.all()  #@UndefinedVariable
    serializer_class = ServiceProviderSerializer
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceProtocolViewSet(viewsets.ModelViewSet):
    queryset = Service_protocol.objects.all()  #@UndefinedVariable
    serializer_class = ServiceProtocolSerializer
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceStatusViewSet(viewsets.ModelViewSet):
    queryset = Service_status.objects.all()  #@UndefinedVariable
    serializer_class = ServiceStatusSerializer
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceTagViewSet(viewsets.ModelViewSet):
    queryset = Service_tag.objects.all()  #@UndefinedVariable
    serializer_class = ServiceTagSerializer
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceBaseViewSet(viewsets.ModelViewSet):
    queryset = Service_base.objects.all()  #@UndefinedVariable
    serializer_class = ServiceBaseSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceBaseFilter
    ordering_fields = ('id','create_time','base_statistics__scores','base_statistics__app_counts')
    def get_queryset(self):
        max_depth = 2
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceFieldTypeViewSet(viewsets.ModelViewSet):
    queryset = Service_fieldType.objects.all()  #@UndefinedVariable
    serializer_class = ServiceFieldTypeSerializer
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceReqFieldViewSet(viewsets.ModelViewSet):
    queryset = Service_reqField.objects.all()  #@UndefinedVariable
    serializer_class = ServiceReqFieldSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceReqFieldFilter
    ordering_fields = ('__all__')
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceRespFieldViewSet(viewsets.ModelViewSet):
    queryset = Service_respField.objects.all()  #@UndefinedVariable
    serializer_class = ServiceRespFieldSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceRespFieldFilter
    ordering_fields = ('__all__')
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceReqDemoViewSet(viewsets.ModelViewSet):
    queryset = Service_reqDemo.objects.all()  #@UndefinedVariable
    serializer_class = ServiceReqDemoSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceReqDemoFilter
    ordering_fields = ('__all__')
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceRespDemoViewSet(viewsets.ModelViewSet):
    queryset = Service_respDemo.objects.all()  #@UndefinedVariable
    serializer_class = ServiceRespDemoSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceRespDemoFilter
    ordering_fields = ('__all__')
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceApiViewSet(viewsets.ModelViewSet):
    queryset = Service_api.objects.all()  #@UndefinedVariable
    serializer_class = ServiceApiSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceAPIFilter
    ordering_fields = ('__all__')
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
#        serve_apis = Service_api.objects.all()
#        if not (self.request.user and self.request.user.is_authenticated()):
#            for serve_api in serve_apis:
#                serve_api.serve_url = None
#        print serve_apis[0].serve_url
        return self.queryset


class ServiceApiSecretViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Service_api.objects.all()  #@UndefinedVariable
    serializer_class = ServiceApiSecretSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceAPISecretFilter
    ordering_fields = ('__all__')
    def get_queryset(self):
        max_depth = 2
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
    
class ServiceErrorTypeViewSet(viewsets.ModelViewSet):
    queryset = Service_errorType.objects.all()  #@UndefinedVariable
    serializer_class = ServiceErrorTypeSerializer
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceErrorCodeViewSet(viewsets.ModelViewSet):
    queryset = Service_errorCode.objects.all()  #@UndefinedVariable
    serializer_class = ServiceErrorCodeSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceErrorCodeFilter
    ordering_fields = ('__all__')
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceUpgradeViewSet(viewsets.ModelViewSet):
    queryset = Service_upgrade.objects.all()  #@UndefinedVariable
    serializer_class = ServiceUpgradeSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceUpgradeFilter
    ordering_fields = ('__all__')
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceStatisticsViewSet(viewsets.ModelViewSet):
    queryset = Service_statistics.objects.all()  #@UndefinedVariable
    serializer_class = ServiceStatisticsSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceStatisticsFilter
    ordering_fields = '__all__'
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
class ServiceContactViewSet(viewsets.ModelViewSet):
    queryset = Service_contact.objects.all()  #@UndefinedVariable
    serializer_class = ServiceContactSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceContactFilter
    ordering_fields = '__all__'
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceOthersViewSet(viewsets.ModelViewSet):
    queryset = Service_others.objects.all()  #@UndefinedVariable
    serializer_class = ServiceOthersSerializer
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
class ServiceInvokeDemoViewSet(viewsets.ModelViewSet):
    queryset = Service_invokeDemo.objects.all()  #@UndefinedVariable
    serializer_class = ServiceInvokeDemoSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceInvokeDemoFilter
    ordering_fields = '__all__'
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class CommonHttpDemoViewSet(viewsets.ModelViewSet):
    queryset = Common_httpDemo.objects.all()  #@UndefinedVariable
    serializer_class = CommonHttpDemoSerializer
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
class ServicePriceViewSet(viewsets.ModelViewSet):
    queryset = Service_price.objects.all()  #@UndefinedVariable
    serializer_class = ServicePriceSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServicePriceFilter
    ordering_fields = '__all__'
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceActivePackViewSet(viewsets.ModelViewSet):
    queryset = Service_activePack.objects.all()  #@UndefinedVariable
    serializer_class = ServiceActivePackSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceActivePackFilter
    ordering_fields = '__all__'
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset
    
    
class ServiceSdkPackViewSet(viewsets.ModelViewSet):
    queryset = Service_sdkPack.objects.all()  #@UndefinedVariable
    serializer_class = ServiceSdkPackSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_class = ServiceSDKPackFilter
    ordering_fields = '__all__'
    def get_queryset(self):
        max_depth = 1
        param_depth = int(self.request.query_params.get('recursion',0))
        if param_depth > max_depth: param_depth = max_depth
        self.serializer_class.Meta.depth = param_depth
        return self.queryset    
    
    
class Cate_Type_Base_ViewSet(viewsets.ReadOnlyModelViewSet): #ReadOnlyModelViewSet只能执行安全方法
    serializer_class = Cate_Type_Base_Serializer
#    authentication_classes = (SessionAuthentication, BasicAuthentication)
#    permission_classes = (JustReadOnly,)
    def get_queryset(self):
        cates = Service_category.objects.all() #@UndefinedVariable
        for cate in cates:
            types = cate.cate_type.all()
            cate.serve_types = types
            for type in types:
                bases = type.type_base.all()
                type.serve_bases = bases
        return cates

